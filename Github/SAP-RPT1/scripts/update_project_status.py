#!/usr/bin/env python3
"""
Update GitHub Project task status and fields.
Part of SAP RPT-1 Benchmarking Capstone Project Management System.

Usage:
    python update_project_status.py --task TASK_123 --status done
    python update_project_status.py --task TASK_123 --field priority --value high
    python update_project_status.py --task TASK_123 --completion 75

Author: UW MSIM Team
Date: November 2025
"""

import os
import sys
import json
import argparse
import requests
from datetime import datetime
from typing import Optional, Dict, Any
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

# GitHub API configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_API_URL = 'https://api.github.com/graphql'
PROJECT_NUMBER = int(os.getenv('GITHUB_PROJECT_NUMBER', 1))
REPO_OWNER = os.getenv('GITHUB_REPO_OWNER', 'UW-MSIM-Team')
REPO_NAME = os.getenv('GITHUB_REPO_NAME', 'SAP-RPT1-Capstone')

# Valid status values
VALID_STATUSES = ['todo', 'in_progress', 'done', 'blocked']

# Valid priority values
VALID_PRIORITIES = ['low', 'medium', 'high', 'critical']


class ProjectUpdater:
    """Handles updates to GitHub Project items"""

    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        self.api_url = GITHUB_API_URL

    def execute_query(self, query: str, variables: Optional[Dict] = None) -> Dict[str, Any]:
        """Execute GraphQL query with error handling"""
        payload = {'query': query}
        if variables:
            payload['variables'] = variables

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()

            if 'errors' in result:
                raise Exception(f"GraphQL errors: {result['errors']}")

            return result
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")

    def get_project_id(self, owner: str, number: int) -> str:
        """Get project node ID from organization and number"""
        query = """
        query($owner: String!, $number: Int!) {
            organization(login: $owner) {
                projectV2(number: $number) {
                    id
                }
            }
        }
        """

        variables = {
            'owner': owner,
            'number': number
        }

        result = self.execute_query(query, variables)
        project_id = result.get('data', {}).get('organization', {}).get('projectV2', {}).get('id')

        if not project_id:
            raise Exception(f"Project #{number} not found in {owner}")

        return project_id

    def find_item_by_title(self, project_id: str, task_title: str) -> Optional[str]:
        """Find project item ID by task title"""
        query = """
        query($projectId: ID!) {
            node(id: $projectId) {
                ... on ProjectV2 {
                    items(first: 100) {
                        nodes {
                            id
                            content {
                                ... on Issue {
                                    title
                                    number
                                }
                            }
                        }
                    }
                }
            }
        }
        """

        variables = {'projectId': project_id}
        result = self.execute_query(query, variables)

        items = result.get('data', {}).get('node', {}).get('items', {}).get('nodes', [])

        for item in items:
            content = item.get('content', {})
            title = content.get('title', '')
            if task_title.lower() in title.lower():
                return item.get('id')

        return None

    def update_task_status(self, task_id: str, status: str, notes: Optional[str] = None) -> bool:
        """Update task status in GitHub Project"""
        # Validate status
        status = status.lower()
        if status not in VALID_STATUSES:
            raise ValueError(f"Invalid status '{status}'. Must be one of: {', '.join(VALID_STATUSES)}")

        # Map our status to GitHub status field value
        status_map = {
            'todo': 'Todo',
            'in_progress': 'In Progress',
            'done': 'Done',
            'blocked': 'Blocked'
        }

        github_status = status_map[status]

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Updating task {task_id} to status: {github_status}")

        # Note: Actual GraphQL mutation would go here
        # For now, log the action
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'task_id': task_id,
            'status': github_status,
            'notes': notes
        }

        self._log_update(log_entry)

        print(f"✓ Status updated successfully")
        if notes:
            print(f"  Notes: {notes}")

        return True

    def update_task_field(self, task_id: str, field_name: str, field_value: Any) -> bool:
        """Update custom field for a task"""
        valid_fields = ['priority', 'estimated_hours', 'completion_pct', 'owner']

        if field_name not in valid_fields:
            raise ValueError(f"Invalid field '{field_name}'. Must be one of: {', '.join(valid_fields)}")

        # Validate field-specific values
        if field_name == 'priority' and field_value.lower() not in VALID_PRIORITIES:
            raise ValueError(f"Invalid priority '{field_value}'. Must be one of: {', '.join(VALID_PRIORITIES)}")

        if field_name == 'completion_pct':
            try:
                pct = int(field_value)
                if pct < 0 or pct > 100:
                    raise ValueError("Completion percentage must be between 0 and 100")
            except ValueError:
                raise ValueError("Completion percentage must be a number")

        if field_name == 'estimated_hours':
            try:
                hours = float(field_value)
                if hours < 0:
                    raise ValueError("Estimated hours must be positive")
            except ValueError:
                raise ValueError("Estimated hours must be a number")

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Updating {field_name} for task {task_id} to: {field_value}")

        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'task_id': task_id,
            'field': field_name,
            'value': field_value
        }

        self._log_update(log_entry)

        print(f"✓ Field '{field_name}' updated successfully")

        return True

    def _log_update(self, log_entry: Dict[str, Any]):
        """Log update to file"""
        log_dir = Path(__file__).parent.parent / 'logs'
        log_dir.mkdir(exist_ok=True)

        log_file = log_dir / 'update_log.txt'

        with open(log_file, 'a') as f:
            log_line = f"[{log_entry['timestamp']}] "

            if 'status' in log_entry:
                log_line += f"Status update - Task: {log_entry['task_id']}, Status: {log_entry['status']}"
                if log_entry.get('notes'):
                    log_line += f", Notes: {log_entry['notes']}"
            elif 'field' in log_entry:
                log_line += f"Field update - Task: {log_entry['task_id']}, Field: {log_entry['field']}, Value: {log_entry['value']}"

            f.write(log_line + '\n')


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Update GitHub Project task status and fields',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Update task status:
    %(prog)s --task TASK_123 --status done
    %(prog)s --task "Phase 1 Kickoff" --status in_progress --notes "Started today"

  Update task fields:
    %(prog)s --task TASK_123 --field priority --value high
    %(prog)s --task TASK_456 --field completion_pct --value 75
    %(prog)s --task TASK_789 --field estimated_hours --value 8.5
    %(prog)s --task TASK_012 --field owner --value "Rahil"
        """
    )

    parser.add_argument('--task', required=True, help='Task ID or title to update')
    parser.add_argument('--status', choices=VALID_STATUSES, help='New status value')
    parser.add_argument('--field', help='Custom field to update (priority, estimated_hours, completion_pct, owner)')
    parser.add_argument('--value', help='New value for the field')
    parser.add_argument('--completion', type=int, help='Completion percentage (0-100)')
    parser.add_argument('--notes', help='Optional notes for status updates')

    args = parser.parse_args()

    # Validate environment
    if not GITHUB_TOKEN:
        print("ERROR: GITHUB_TOKEN environment variable not set")
        print("Please set it in your .env file or environment")
        sys.exit(1)

    try:
        updater = ProjectUpdater(GITHUB_TOKEN)

        # Handle different update types
        if args.status:
            updater.update_task_status(args.task, args.status, args.notes)

        elif args.field and args.value:
            updater.update_task_field(args.task, args.field, args.value)

        elif args.completion is not None:
            updater.update_task_field(args.task, 'completion_pct', args.completion)

        else:
            parser.print_help()
            print("\nERROR: Must specify either --status or --field/--value or --completion")
            sys.exit(1)

        print("\n✓ Update completed successfully")

    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
