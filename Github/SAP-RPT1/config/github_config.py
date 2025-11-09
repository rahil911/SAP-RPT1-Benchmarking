"""
Configuration Management for SAP RPT-1 GitHub Projects.
Loads and validates all required settings from environment variables.

This module provides centralized configuration for:
- GitHub API credentials
- Repository settings
- Project parameters
- Rate limiting
- File paths and directories

Author: UW MSIM Team
Date: November 2025
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any
from dotenv import load_dotenv

# Load .env file from project root
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


class GitHubConfig:
    """
    GitHub API and Project configuration.

    Loads settings from environment variables with validation.
    Required variables must be set in .env file or system environment.
    """

    # ============================================================================
    # REQUIRED SETTINGS
    # ============================================================================

    GITHUB_TOKEN: str = os.getenv('GITHUB_TOKEN', '')
    """GitHub Personal Access Token with project and repo permissions"""

    REPO_OWNER: str = os.getenv('GITHUB_REPO_OWNER', 'UW-MSIM-Team')
    """GitHub organization or username that owns the repository"""

    REPO_NAME: str = os.getenv('GITHUB_REPO_NAME', 'SAP-RPT1-Capstone')
    """Repository name where issues will be created"""

    # ============================================================================
    # OPTIONAL SETTINGS WITH DEFAULTS
    # ============================================================================

    PROJECT_NUMBER: int = int(os.getenv('GITHUB_PROJECT_NUMBER', '1'))
    """Project board number (visible in GitHub Projects URL)"""

    PROJECT_TITLE: str = os.getenv('PROJECT_TITLE', 'SAP RPT-1 Benchmarking')
    """Human-readable project title"""

    # ============================================================================
    # API RATE LIMITING
    # ============================================================================

    RATE_LIMIT_DELAY: int = int(os.getenv('RATE_LIMIT_DELAY', '1'))
    """Delay in seconds between API requests (default: 1s)"""

    MAX_RETRIES: int = int(os.getenv('MAX_RETRIES', '3'))
    """Maximum number of retry attempts for failed requests"""

    RETRY_BACKOFF: int = int(os.getenv('RETRY_BACKOFF', '2'))
    """Exponential backoff multiplier for retries"""

    REQUEST_TIMEOUT: int = int(os.getenv('REQUEST_TIMEOUT', '30'))
    """HTTP request timeout in seconds"""

    # ============================================================================
    # GITHUB API ENDPOINTS
    # ============================================================================

    GRAPHQL_ENDPOINT: str = 'https://api.github.com/graphql'
    """GitHub GraphQL API v4 endpoint"""

    REST_ENDPOINT: str = 'https://api.github.com'
    """GitHub REST API v3 base URL"""

    # ============================================================================
    # PROJECT FIELD NAMES
    # ============================================================================

    STATUS_FIELD: str = os.getenv('STATUS_FIELD_NAME', 'Status')
    """Name of status field in GitHub Project"""

    PRIORITY_FIELD: str = os.getenv('PRIORITY_FIELD_NAME', 'Priority')
    """Name of priority field in GitHub Project"""

    PHASE_FIELD: str = os.getenv('PHASE_FIELD_NAME', 'Phase')
    """Name of phase field in GitHub Project"""

    OWNER_FIELD: str = os.getenv('OWNER_FIELD_NAME', 'Owner')
    """Name of owner/assignee field in GitHub Project"""

    # ============================================================================
    # STATUS VALUES
    # ============================================================================

    STATUS_TODO: str = 'Todo'
    STATUS_IN_PROGRESS: str = 'In Progress'
    STATUS_DONE: str = 'Done'
    STATUS_BLOCKED: str = 'Blocked'

    VALID_STATUSES = [STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE, STATUS_BLOCKED]

    # ============================================================================
    # PRIORITY VALUES
    # ============================================================================

    PRIORITY_LOW: str = 'Low'
    PRIORITY_MEDIUM: str = 'Medium'
    PRIORITY_HIGH: str = 'High'
    PRIORITY_CRITICAL: str = 'Critical'

    VALID_PRIORITIES = [PRIORITY_LOW, PRIORITY_MEDIUM, PRIORITY_HIGH, PRIORITY_CRITICAL]

    # ============================================================================
    # VALIDATION METHODS
    # ============================================================================

    @classmethod
    def validate(cls) -> bool:
        """
        Validate all required settings are present and valid.

        Returns:
            True if all validations pass

        Raises:
            ValueError: If required settings are missing or invalid
        """
        errors = []

        # Check required settings
        required = {
            'GITHUB_TOKEN': cls.GITHUB_TOKEN,
            'REPO_OWNER': cls.REPO_OWNER,
            'REPO_NAME': cls.REPO_NAME
        }

        for name, value in required.items():
            if not value:
                errors.append(f"Missing required setting: {name}")

        # Validate token format (should start with 'ghp_' or 'github_pat_')
        if cls.GITHUB_TOKEN and not (
            cls.GITHUB_TOKEN.startswith('ghp_') or
            cls.GITHUB_TOKEN.startswith('github_pat_')
        ):
            errors.append(
                "GITHUB_TOKEN format invalid. Should start with 'ghp_' or 'github_pat_'"
            )

        # Validate numeric settings
        if cls.PROJECT_NUMBER < 1:
            errors.append("PROJECT_NUMBER must be >= 1")

        if cls.RATE_LIMIT_DELAY < 0:
            errors.append("RATE_LIMIT_DELAY must be >= 0")

        if cls.MAX_RETRIES < 1:
            errors.append("MAX_RETRIES must be >= 1")

        if cls.REQUEST_TIMEOUT < 1:
            errors.append("REQUEST_TIMEOUT must be >= 1")

        if errors:
            error_msg = "Configuration validation failed:\n  - " + "\n  - ".join(errors)
            raise ValueError(error_msg)

        return True

    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        """
        Export configuration as dictionary (excluding sensitive data).

        Returns:
            Dictionary of configuration values
        """
        return {
            'repo_owner': cls.REPO_OWNER,
            'repo_name': cls.REPO_NAME,
            'project_number': cls.PROJECT_NUMBER,
            'project_title': cls.PROJECT_TITLE,
            'rate_limit_delay': cls.RATE_LIMIT_DELAY,
            'max_retries': cls.MAX_RETRIES,
            'retry_backoff': cls.RETRY_BACKOFF,
            'request_timeout': cls.REQUEST_TIMEOUT,
            'graphql_endpoint': cls.GRAPHQL_ENDPOINT,
            'rest_endpoint': cls.REST_ENDPOINT,
            'status_field': cls.STATUS_FIELD,
            'priority_field': cls.PRIORITY_FIELD,
            'phase_field': cls.PHASE_FIELD,
            'owner_field': cls.OWNER_FIELD,
            'token_set': bool(cls.GITHUB_TOKEN)  # Don't expose actual token
        }

    @classmethod
    def get_repo_url(cls) -> str:
        """Get full repository URL"""
        return f"https://github.com/{cls.REPO_OWNER}/{cls.REPO_NAME}"

    @classmethod
    def get_project_url(cls) -> str:
        """Get full project board URL"""
        return f"https://github.com/orgs/{cls.REPO_OWNER}/projects/{cls.PROJECT_NUMBER}"


class ProjectConfig:
    """
    Project-specific settings and paths.

    Manages file system paths and project structure.
    Automatically creates required directories on initialization.
    """

    # ============================================================================
    # BASE PATHS
    # ============================================================================

    BASE_DIR: Path = Path(__file__).parent.parent
    """Project root directory"""

    DATA_DIR: Path = BASE_DIR / 'data' / 'weeks'
    """Directory containing week JSON data files"""

    DELIVERABLES_DIR: Path = BASE_DIR / 'deliverables'
    """Directory for output files (Excel, reports, etc.)"""

    LOGS_DIR: Path = BASE_DIR / 'logs'
    """Directory for log files"""

    SCRIPTS_DIR: Path = BASE_DIR / 'scripts'
    """Directory containing automation scripts"""

    UTILS_DIR: Path = BASE_DIR / 'utils'
    """Directory containing utility modules"""

    CONFIG_DIR: Path = BASE_DIR / 'config'
    """Directory containing configuration files"""

    # ============================================================================
    # FILE PATHS
    # ============================================================================

    TIMELINE_EXCEL: Path = DELIVERABLES_DIR / 'sap-project-timeline.xlsx'
    """Excel timeline spreadsheet"""

    IMPORT_LOG: Path = LOGS_DIR / 'import_log.txt'
    """GitHub import execution log"""

    UPDATE_LOG: Path = LOGS_DIR / 'update_log.txt'
    """Task update log"""

    ERROR_LOG: Path = LOGS_DIR / 'error_log.txt'
    """Error and exception log"""

    # ============================================================================
    # PROJECT METADATA
    # ============================================================================

    PROJECT_DURATION_WEEKS: int = 12
    """Total project duration in weeks"""

    TOTAL_TASKS: int = 150
    """Total number of tasks across all weeks"""

    START_DATE: str = '2026-01-06'
    """Project start date (ISO format)"""

    END_DATE: str = '2026-03-30'
    """Project end date (ISO format)"""

    TEAM_SIZE: int = 4
    """Number of team members"""

    # ============================================================================
    # DIRECTORY MANAGEMENT
    # ============================================================================

    @classmethod
    def ensure_directories(cls) -> None:
        """
        Create required directories if they don't exist.

        Creates all directories defined in path attributes.
        Safe to call multiple times (idempotent).
        """
        directories = [
            cls.DATA_DIR,
            cls.DELIVERABLES_DIR,
            cls.LOGS_DIR,
            cls.SCRIPTS_DIR,
            cls.UTILS_DIR,
            cls.CONFIG_DIR
        ]

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)

    @classmethod
    def get_week_file(cls, week_number: int) -> Path:
        """
        Get path to week data JSON file.

        Args:
            week_number: Week number (1-12)

        Returns:
            Path to week JSON file

        Raises:
            ValueError: If week number out of range
        """
        if not 1 <= week_number <= cls.PROJECT_DURATION_WEEKS:
            raise ValueError(
                f"Week number must be between 1 and {cls.PROJECT_DURATION_WEEKS}"
            )

        return cls.DATA_DIR / f'week_{week_number:02d}.json'

    @classmethod
    def get_all_week_files(cls) -> list[Path]:
        """
        Get paths to all week JSON files.

        Returns:
            List of Path objects for weeks 1-12
        """
        return [cls.get_week_file(i) for i in range(1, cls.PROJECT_DURATION_WEEKS + 1)]

    @classmethod
    def to_dict(cls) -> Dict[str, Any]:
        """
        Export project configuration as dictionary.

        Returns:
            Dictionary of project settings
        """
        return {
            'base_dir': str(cls.BASE_DIR),
            'data_dir': str(cls.DATA_DIR),
            'deliverables_dir': str(cls.DELIVERABLES_DIR),
            'logs_dir': str(cls.LOGS_DIR),
            'project_duration_weeks': cls.PROJECT_DURATION_WEEKS,
            'total_tasks': cls.TOTAL_TASKS,
            'start_date': cls.START_DATE,
            'end_date': cls.END_DATE,
            'team_size': cls.TEAM_SIZE
        }


# ============================================================================
# INITIALIZATION
# ============================================================================

# Ensure directories exist on module import
ProjectConfig.ensure_directories()

# Validate GitHub configuration (will raise ValueError if invalid)
try:
    GitHubConfig.validate()
except ValueError as e:
    # Print warning but don't crash - allows importing for documentation/testing
    print(f"WARNING: {e}")
    print("Please check your .env file and ensure all required variables are set.")


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def get_config_summary() -> Dict[str, Any]:
    """
    Get summary of all configuration settings.

    Returns:
        Dictionary with GitHub and project settings
    """
    return {
        'github': GitHubConfig.to_dict(),
        'project': ProjectConfig.to_dict()
    }


def print_config_summary() -> None:
    """Print formatted configuration summary to console"""
    config = get_config_summary()

    print("\n" + "=" * 70)
    print("SAP RPT-1 GitHub Projects - Configuration Summary")
    print("=" * 70)

    print("\nGitHub Settings:")
    for key, value in config['github'].items():
        print(f"  {key:20s}: {value}")

    print("\nProject Settings:")
    for key, value in config['project'].items():
        print(f"  {key:20s}: {value}")

    print("\n" + "=" * 70 + "\n")


# Example usage
if __name__ == "__main__":
    print_config_summary()
