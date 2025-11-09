"""
GitHub API Wrapper for Project Management.
Provides reusable methods for GraphQL operations with rate limiting and error handling.

This module wraps the GitHub GraphQL API v4 for managing Projects V2,
including creating items, updating statuses, and managing custom fields.

Author: UW MSIM Team
Date: November 2025
"""

import requests
import time
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class GitHubAPIError(Exception):
    """Custom exception for GitHub API errors"""
    pass


class RateLimitError(GitHubAPIError):
    """Exception raised when rate limit is exceeded"""
    pass


class GitHubProjectAPI:
    """
    Wrapper for GitHub GraphQL API with rate limiting and error handling.

    Provides methods for:
    - Project queries and mutations
    - Issue creation and management
    - Project item operations
    - Custom field updates
    - Rate limit monitoring
    """

    def __init__(
        self,
        token: str,
        org: Optional[str] = None,
        repo: Optional[str] = None,
        max_retries: int = 3,
        retry_delay: int = 2
    ):
        """
        Initialize GitHub API wrapper.

        Args:
            token: GitHub personal access token with project permissions
            org: GitHub organization name (optional)
            repo: Repository name (optional)
            max_retries: Maximum number of retry attempts
            retry_delay: Base delay between retries in seconds
        """
        self.token = token
        self.org = org
        self.repo = repo
        self.max_retries = max_retries
        self.retry_delay = retry_delay

        self.api_url = 'https://api.github.com/graphql'
        self.rest_api_url = 'https://api.github.com'

        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.github.v3+json'
        }

        # Cache for frequently accessed data
        self._project_cache: Dict[int, str] = {}
        self._field_cache: Dict[str, Dict] = {}

        logger.info("GitHub API wrapper initialized")

    def execute_query(
        self,
        query: str,
        variables: Optional[Dict] = None,
        retry_on_rate_limit: bool = True
    ) -> Dict[str, Any]:
        """
        Execute GraphQL query with error handling and retries.

        Args:
            query: GraphQL query string
            variables: Query variables dictionary
            retry_on_rate_limit: Whether to retry on rate limit errors

        Returns:
            Response data dictionary

        Raises:
            GitHubAPIError: On API errors
            RateLimitError: On rate limit exceeded (if retry disabled)
        """
        payload = {'query': query}
        if variables:
            payload['variables'] = variables

        for attempt in range(self.max_retries):
            try:
                response = requests.post(
                    self.api_url,
                    headers=self.headers,
                    json=payload,
                    timeout=30
                )

                # Handle rate limiting
                if response.status_code == 403:
                    rate_limit_remaining = response.headers.get('X-RateLimit-Remaining', 0)
                    if int(rate_limit_remaining) == 0:
                        if not retry_on_rate_limit:
                            raise RateLimitError("GitHub API rate limit exceeded")

                        reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
                        wait_time = max(reset_time - time.time(), 60)

                        logger.warning(f"Rate limit exceeded. Waiting {wait_time:.0f}s...")
                        time.sleep(wait_time)
                        continue

                response.raise_for_status()
                result = response.json()

                # Check for GraphQL errors
                if 'errors' in result:
                    error_messages = [e.get('message', str(e)) for e in result['errors']]
                    raise GitHubAPIError(f"GraphQL errors: {'; '.join(error_messages)}")

                return result

            except requests.exceptions.Timeout:
                logger.warning(f"Request timeout (attempt {attempt + 1}/{self.max_retries})")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (2 ** attempt))  # Exponential backoff
                    continue
                raise GitHubAPIError("Request timed out after multiple retries")

            except requests.exceptions.RequestException as e:
                if attempt < self.max_retries - 1:
                    logger.warning(f"Request failed (attempt {attempt + 1}/{self.max_retries}): {str(e)}")
                    time.sleep(self.retry_delay * (2 ** attempt))
                    continue
                raise GitHubAPIError(f"API request failed: {str(e)}")

        raise GitHubAPIError("Maximum retries exceeded")

    def get_project_id(self, project_number: int, owner: Optional[str] = None) -> str:
        """
        Get project node ID from project number.

        Args:
            project_number: Project number (visible in URL)
            owner: Organization or user login (uses self.org if not provided)

        Returns:
            Project node ID (used in GraphQL mutations)

        Raises:
            GitHubAPIError: If project not found
        """
        # Check cache
        if project_number in self._project_cache:
            logger.debug(f"Using cached project ID for #{project_number}")
            return self._project_cache[project_number]

        owner = owner or self.org
        if not owner:
            raise GitHubAPIError("Owner/organization not specified")

        query = """
        query($owner: String!, $number: Int!) {
            organization(login: $owner) {
                projectV2(number: $number) {
                    id
                    title
                }
            }
        }
        """

        variables = {
            'owner': owner,
            'number': project_number
        }

        result = self.execute_query(query, variables)
        project_data = result.get('data', {}).get('organization', {}).get('projectV2')

        if not project_data:
            raise GitHubAPIError(f"Project #{project_number} not found in {owner}")

        project_id = project_data['id']
        project_title = project_data.get('title', 'Unknown')

        # Cache the result
        self._project_cache[project_number] = project_id

        logger.info(f"Found project: {project_title} (#{project_number})")
        return project_id

    def create_issue(
        self,
        title: str,
        body: Optional[str] = None,
        labels: Optional[List[str]] = None,
        assignees: Optional[List[str]] = None
    ) -> str:
        """
        Create GitHub issue using REST API.

        Args:
            title: Issue title
            body: Issue description
            labels: List of label names
            assignees: List of GitHub usernames

        Returns:
            Issue node ID

        Raises:
            GitHubAPIError: On creation failure
        """
        if not self.org or not self.repo:
            raise GitHubAPIError("Repository owner and name required")

        url = f"{self.rest_api_url}/repos/{self.org}/{self.repo}/issues"

        payload = {'title': title}
        if body:
            payload['body'] = body
        if labels:
            payload['labels'] = labels
        if assignees:
            payload['assignees'] = assignees

        try:
            response = requests.post(url, headers=self.headers, json=payload, timeout=30)
            response.raise_for_status()
            issue_data = response.json()

            logger.info(f"Created issue #{issue_data['number']}: {title}")
            return issue_data['node_id']

        except requests.exceptions.RequestException as e:
            raise GitHubAPIError(f"Failed to create issue: {str(e)}")

    def create_project_item(self, project_id: str, issue_id: str) -> str:
        """
        Add issue to project board.

        Args:
            project_id: Project node ID
            issue_id: Issue node ID

        Returns:
            Project item ID

        Raises:
            GitHubAPIError: On failure
        """
        mutation = """
        mutation($projectId: ID!, $contentId: ID!) {
            addProjectV2ItemById(input: {projectId: $projectId, contentId: $contentId}) {
                item {
                    id
                }
            }
        }
        """

        variables = {
            'projectId': project_id,
            'contentId': issue_id
        }

        result = self.execute_query(mutation, variables)
        item_data = result.get('data', {}).get('addProjectV2ItemById', {}).get('item')

        if not item_data:
            raise GitHubAPIError("Failed to add item to project")

        item_id = item_data['id']
        logger.info(f"Added item to project: {item_id}")
        return item_id

    def update_item_status(self, project_id: str, item_id: str, status: str):
        """
        Update project item status field.

        Args:
            project_id: Project node ID
            item_id: Project item ID
            status: Status value (e.g., "Todo", "In Progress", "Done")

        Raises:
            GitHubAPIError: On update failure
        """
        # Get status field ID
        field_id = self._get_field_id(project_id, 'Status')

        mutation = """
        mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $value: ProjectV2FieldValue!) {
            updateProjectV2ItemFieldValue(
                input: {
                    projectId: $projectId
                    itemId: $itemId
                    fieldId: $fieldId
                    value: $value
                }
            ) {
                projectV2Item {
                    id
                }
            }
        }
        """

        variables = {
            'projectId': project_id,
            'itemId': item_id,
            'fieldId': field_id,
            'value': {'singleSelectOptionId': status}
        }

        self.execute_query(mutation, variables)
        logger.info(f"Updated item {item_id} status to: {status}")

    def _get_field_id(self, project_id: str, field_name: str) -> str:
        """
        Get custom field ID by name.

        Args:
            project_id: Project node ID
            field_name: Field name to look up

        Returns:
            Field ID

        Raises:
            GitHubAPIError: If field not found
        """
        cache_key = f"{project_id}:{field_name}"
        if cache_key in self._field_cache:
            return self._field_cache[cache_key]['id']

        query = """
        query($projectId: ID!) {
            node(id: $projectId) {
                ... on ProjectV2 {
                    fields(first: 20) {
                        nodes {
                            ... on ProjectV2Field {
                                id
                                name
                            }
                            ... on ProjectV2SingleSelectField {
                                id
                                name
                            }
                        }
                    }
                }
            }
        }
        """

        result = self.execute_query(query, {'projectId': project_id})
        fields = result.get('data', {}).get('node', {}).get('fields', {}).get('nodes', [])

        for field in fields:
            if field.get('name') == field_name:
                self._field_cache[cache_key] = field
                return field['id']

        raise GitHubAPIError(f"Field '{field_name}' not found in project")

    def get_rate_limit_status(self) -> Dict[str, Any]:
        """
        Check GitHub API rate limit status.

        Returns:
            Dictionary with rate limit info:
            - limit: Total requests allowed per hour
            - remaining: Requests remaining
            - reset: Timestamp when limit resets
            - used: Requests used
        """
        query = """
        query {
            rateLimit {
                limit
                remaining
                resetAt
                used
            }
        }
        """

        result = self.execute_query(query)
        rate_limit = result.get('data', {}).get('rateLimit', {})

        logger.info(
            f"Rate limit: {rate_limit.get('remaining', 0)}/{rate_limit.get('limit', 0)} remaining"
        )

        return rate_limit

    def get_project_items(
        self,
        project_id: str,
        first: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Get all items in a project.

        Args:
            project_id: Project node ID
            first: Number of items to fetch (max 100)

        Returns:
            List of project items with content
        """
        query = """
        query($projectId: ID!, $first: Int!) {
            node(id: $projectId) {
                ... on ProjectV2 {
                    items(first: $first) {
                        nodes {
                            id
                            content {
                                ... on Issue {
                                    id
                                    title
                                    number
                                    state
                                    url
                                }
                            }
                        }
                    }
                }
            }
        }
        """

        variables = {
            'projectId': project_id,
            'first': first
        }

        result = self.execute_query(query, variables)
        items = result.get('data', {}).get('node', {}).get('items', {}).get('nodes', [])

        logger.info(f"Retrieved {len(items)} project items")
        return items


# Example usage
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    # Initialize API wrapper
    api = GitHubProjectAPI(
        token=os.getenv('GITHUB_TOKEN'),
        org=os.getenv('GITHUB_REPO_OWNER'),
        repo=os.getenv('GITHUB_REPO_NAME')
    )

    # Check rate limit
    rate_limit = api.get_rate_limit_status()
    print(f"\nRate Limit Status:")
    print(f"  Remaining: {rate_limit.get('remaining')}/{rate_limit.get('limit')}")
    print(f"  Resets at: {rate_limit.get('resetAt')}")

    # Get project ID
    try:
        project_id = api.get_project_id(1)
        print(f"\nProject ID: {project_id}")

        # Get project items
        items = api.get_project_items(project_id, first=10)
        print(f"\nFound {len(items)} items in project")

    except GitHubAPIError as e:
        print(f"Error: {e}")
