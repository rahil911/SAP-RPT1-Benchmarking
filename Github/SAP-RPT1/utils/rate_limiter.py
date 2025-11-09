"""
Rate Limiting Utility for GitHub API.
Implements token bucket algorithm with exponential backoff to prevent API rate limit violations.

This module provides:
- Token bucket rate limiting
- Exponential backoff retry logic
- GitHub secondary rate limit handling
- Automatic rate limit recovery

GitHub API Rate Limits:
- GraphQL API: 5,000 points per hour
- REST API: 5,000 requests per hour
- Secondary rate limits: Variable based on endpoint

Author: UW MSIM Team
Date: November 2025
"""

import time
import logging
from datetime import datetime, timedelta
from typing import Callable, Any, Optional
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class RateLimitExceeded(Exception):
    """Exception raised when rate limit is exceeded and retries exhausted"""
    pass


class RateLimiter:
    """
    Token bucket rate limiter with exponential backoff.

    Implements a token bucket algorithm to smooth out API requests
    and prevent hitting rate limits. Supports automatic backoff and retry
    on rate limit errors.

    Attributes:
        max_requests: Maximum requests allowed per time window
        time_window: Time window in seconds (default: 3600 = 1 hour)
        retry_limit: Maximum number of retry attempts
        tokens: Current number of available tokens
        last_refill: Timestamp of last token refill
    """

    def __init__(
        self,
        max_requests: int = 5000,  # GitHub default
        time_window: int = 3600,   # 1 hour in seconds
        retry_limit: int = 3,
        min_delay: float = 0.5     # Minimum delay between requests
    ):
        """
        Initialize rate limiter.

        Args:
            max_requests: Maximum requests per time window
            time_window: Time window in seconds
            retry_limit: Maximum retry attempts
            min_delay: Minimum delay between requests in seconds
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.retry_limit = retry_limit
        self.min_delay = min_delay

        # Token bucket state
        self.tokens = float(max_requests)
        self.last_refill = datetime.now()

        # Statistics
        self.total_requests = 0
        self.total_retries = 0
        self.total_wait_time = 0.0

        logger.info(
            f"Rate limiter initialized: {max_requests} requests per "
            f"{time_window}s window"
        )

    def _refill_tokens(self) -> None:
        """
        Refill token bucket based on elapsed time.

        Tokens are added proportionally to time elapsed since last refill.
        Uses linear refill rate: tokens_per_second = max_requests / time_window
        """
        now = datetime.now()
        elapsed = (now - self.last_refill).total_seconds()

        if elapsed <= 0:
            return

        # Calculate tokens to add based on elapsed time
        tokens_per_second = self.max_requests / self.time_window
        tokens_to_add = elapsed * tokens_per_second

        # Add tokens, capped at maximum
        self.tokens = min(self.max_requests, self.tokens + tokens_to_add)
        self.last_refill = now

        logger.debug(f"Refilled {tokens_to_add:.2f} tokens, current: {self.tokens:.2f}")

    def acquire(self, tokens: int = 1, block: bool = True) -> bool:
        """
        Attempt to acquire tokens from the bucket.

        Args:
            tokens: Number of tokens to acquire
            block: If True, wait until tokens available; if False, return immediately

        Returns:
            True if tokens acquired, False if not available and block=False

        Raises:
            ValueError: If tokens requested exceeds maximum
        """
        if tokens > self.max_requests:
            raise ValueError(
                f"Requested {tokens} tokens exceeds maximum {self.max_requests}"
            )

        self._refill_tokens()

        if self.tokens >= tokens:
            # Tokens available, acquire immediately
            self.tokens -= tokens
            self.total_requests += 1

            # Apply minimum delay
            if self.min_delay > 0:
                time.sleep(self.min_delay)

            logger.debug(f"Acquired {tokens} tokens, {self.tokens:.2f} remaining")
            return True

        elif not block:
            # Non-blocking mode, return failure
            return False

        else:
            # Blocking mode, wait for tokens
            deficit = tokens - self.tokens
            wait_time = (deficit / self.max_requests) * self.time_window

            logger.warning(
                f"Rate limit approaching, waiting {wait_time:.1f}s for {tokens} tokens"
            )

            time.sleep(wait_time)
            self.total_wait_time += wait_time

            # Try again after waiting
            self._refill_tokens()
            self.tokens -= tokens
            self.total_requests += 1

            logger.debug(f"Acquired {tokens} tokens after waiting")
            return True

    def with_backoff(
        self,
        func: Callable,
        *args,
        **kwargs
    ) -> Any:
        """
        Execute function with exponential backoff on rate limit errors.

        Automatically retries on rate limit errors (HTTP 403, 429) with
        exponential backoff: 1s, 2s, 4s, 8s, etc.

        Args:
            func: Function to execute
            *args: Positional arguments for function
            **kwargs: Keyword arguments for function

        Returns:
            Function return value

        Raises:
            RateLimitExceeded: If retries exhausted
            Exception: Any other exception from function
        """
        last_exception = None

        for attempt in range(self.retry_limit):
            try:
                # Acquire token before request
                self.acquire()

                # Execute function
                result = func(*args, **kwargs)

                # Success, reset retry counter
                if attempt > 0:
                    logger.info(f"Request succeeded after {attempt} retries")

                return result

            except Exception as e:
                last_exception = e
                error_str = str(e).lower()

                # Check if rate limit error
                is_rate_limit = (
                    '403' in error_str or
                    '429' in error_str or
                    'rate limit' in error_str or
                    'too many requests' in error_str
                )

                if not is_rate_limit:
                    # Not a rate limit error, propagate immediately
                    raise

                # Rate limit error, apply exponential backoff
                if attempt < self.retry_limit - 1:
                    wait = 2 ** attempt  # Exponential: 1s, 2s, 4s, 8s
                    self.total_retries += 1

                    logger.warning(
                        f"Rate limited, retry {attempt + 1}/{self.retry_limit} "
                        f"in {wait}s: {e}"
                    )

                    time.sleep(wait)
                    self.total_wait_time += wait

                    # Refill tokens after waiting
                    self._refill_tokens()
                else:
                    # Retries exhausted
                    logger.error(
                        f"Rate limit retries exhausted after {self.retry_limit} attempts"
                    )

        # All retries failed
        raise RateLimitExceeded(
            f"Failed after {self.retry_limit} retries: {last_exception}"
        )

    def get_statistics(self) -> dict:
        """
        Get rate limiter statistics.

        Returns:
            Dictionary with usage statistics
        """
        return {
            'total_requests': self.total_requests,
            'total_retries': self.total_retries,
            'total_wait_time': self.total_wait_time,
            'current_tokens': self.tokens,
            'max_tokens': self.max_requests,
            'utilization_pct': (1 - self.tokens / self.max_requests) * 100
        }

    def reset(self) -> None:
        """Reset rate limiter to initial state"""
        self.tokens = float(self.max_requests)
        self.last_refill = datetime.now()
        self.total_requests = 0
        self.total_retries = 0
        self.total_wait_time = 0.0
        logger.info("Rate limiter reset")


# ============================================================================
# DECORATOR FOR RATE LIMITED FUNCTIONS
# ============================================================================

def rate_limited(
    limiter: Optional[RateLimiter] = None,
    tokens: int = 1
) -> Callable:
    """
    Decorator to apply rate limiting to a function.

    Args:
        limiter: RateLimiter instance (uses global if None)
        tokens: Number of tokens to acquire per call

    Returns:
        Decorated function

    Example:
        @rate_limited(tokens=2)
        def expensive_api_call():
            # This will acquire 2 tokens before executing
            pass
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            rate_limiter = limiter or github_limiter
            return rate_limiter.with_backoff(func, *args, **kwargs)
        return wrapper
    return decorator


# ============================================================================
# GLOBAL RATE LIMITER INSTANCES
# ============================================================================

# GitHub GraphQL API rate limiter (5000 points per hour)
github_limiter = RateLimiter(
    max_requests=5000,
    time_window=3600,
    retry_limit=3,
    min_delay=0.5
)

# GitHub REST API rate limiter (5000 requests per hour)
github_rest_limiter = RateLimiter(
    max_requests=5000,
    time_window=3600,
    retry_limit=3,
    min_delay=0.5
)

# Conservative rate limiter for bulk operations (1 request per second)
conservative_limiter = RateLimiter(
    max_requests=3600,
    time_window=3600,
    retry_limit=5,
    min_delay=1.0
)


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def wait_for_rate_limit_reset(reset_timestamp: int) -> None:
    """
    Wait until GitHub rate limit resets.

    Args:
        reset_timestamp: Unix timestamp when rate limit resets
    """
    now = int(time.time())
    wait_time = max(reset_timestamp - now, 0)

    if wait_time > 0:
        logger.warning(
            f"Rate limit exceeded. Waiting {wait_time}s until reset at "
            f"{datetime.fromtimestamp(reset_timestamp).strftime('%H:%M:%S')}"
        )
        time.sleep(wait_time + 1)  # Add 1 second buffer
    else:
        logger.info("Rate limit already reset")


def get_all_limiter_stats() -> dict:
    """
    Get statistics for all global rate limiters.

    Returns:
        Dictionary with stats for each limiter
    """
    return {
        'github_graphql': github_limiter.get_statistics(),
        'github_rest': github_rest_limiter.get_statistics(),
        'conservative': conservative_limiter.get_statistics()
    }


def print_limiter_stats() -> None:
    """Print formatted statistics for all rate limiters"""
    stats = get_all_limiter_stats()

    print("\n" + "=" * 70)
    print("Rate Limiter Statistics")
    print("=" * 70)

    for name, stat in stats.items():
        print(f"\n{name.upper()}:")
        print(f"  Total requests:  {stat['total_requests']}")
        print(f"  Total retries:   {stat['total_retries']}")
        print(f"  Total wait time: {stat['total_wait_time']:.1f}s")
        print(f"  Current tokens:  {stat['current_tokens']:.0f}/{stat['max_tokens']}")
        print(f"  Utilization:     {stat['utilization_pct']:.1f}%")

    print("\n" + "=" * 70 + "\n")


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    import requests

    # Example: Rate limited API call
    @rate_limited(github_limiter, tokens=1)
    def make_api_call(url: str) -> dict:
        """Example API call with rate limiting"""
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    # Example: Manual rate limiting
    limiter = RateLimiter(max_requests=10, time_window=60)

    print("Making 15 requests with rate limit of 10 per minute...")
    for i in range(15):
        limiter.acquire()
        print(f"Request {i + 1} - Tokens remaining: {limiter.tokens:.1f}")

    # Print statistics
    print_limiter_stats()
