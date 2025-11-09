#!/usr/bin/env python3
"""
import_tasks_to_github.py
Import tasks from week JSON files to GitHub Issues

This script reads task data from week JSON files and creates GitHub Issues
with proper labels, assignees, and metadata.

Usage:
    python3 import_tasks_to_github.py
    python3 import_tasks_to_github.py --week 1  # Import specific week only

Prerequisites:
    - GitHub CLI (gh) installed and authenticated
    - Repository specified in environment: REPO_OWNER, REPO_NAME

Author: Agent 5 (GitHub Projects Manager)
Date: 2025-11-08
"""

import os
import json
import subprocess
import argparse
from pathlib import Path
from time import sleep


# GitHub username mapping (update with actual usernames)
GITHUB_USERNAME_MAP = {
    'Rahil M. Harihar': 'rahilharihar',
    'Siddarth Bhave': 'siddarth-bhave',
    'Mathew Jerry Meleth': 'mathew-meleth',
    'Shreyas B Subramanya': 'shreyas-subramanya'
}


def get_repo_info():
    """Get repository owner and name from environment or current repo"""
    owner = os.getenv('REPO_OWNER')
    name = os.getenv('REPO_NAME')

    if not owner or not name:
        print("⚠️  REPO_OWNER or REPO_NAME not set")
        print("   Using current repository...")

        try:
            result = subprocess.run(
                ['gh', 'repo', 'view', '--json', 'owner,name'],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                repo_info = json.loads(result.stdout)
                owner = repo_info['owner']['login']
                name = repo_info['name']
                print(f"   Found: {owner}/{name}")
            else:
                print("❌ Could not determine repository")
                return None, None

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None, None

    return owner, name


def create_issue_with_cli(repo_owner, repo_name, task, week_data):
    """Create GitHub Issue using GitHub CLI"""

    # Map owner name to GitHub username
    assignee = GITHUB_USERNAME_MAP.get(task['owner'], task['owner'].lower().replace(' ', '-'))

    # Prepare issue body
    body = f"""## Description
{task['description']}

## Deliverable
`{task['deliverable']}`

## Success Criteria
{task['success_criteria']}

## Metadata
- **Owner**: {task['owner']}
- **Estimated Hours**: {task['estimated_hours']}
- **Priority**: {task['priority']}
- **Week**: {week_data['week']}
- **Phase**: {week_data['phase']}
- **Dependencies**: {', '.join(task['dependencies']) if task['dependencies'] else 'None'}

## Tools Required
{', '.join(task.get('tools', []))}

---
*Auto-generated from week_{week_data['week']:02d}.json*
"""

    # Create labels
    labels = [
        week_data['phase'].lower().replace(' ', '-'),
        task['priority'].lower(),
        f"week-{week_data['week']:02d}"
    ]

    # Build gh CLI command
    title = f"[{task['id']}] {task['title']}"

    cmd = [
        'gh', 'issue', 'create',
        '--repo', f"{repo_owner}/{repo_name}",
        '--title', title,
        '--body', body,
        '--label', ','.join(labels)
    ]

    # Add assignee if mapping exists
    if assignee:
        cmd.extend(['--assignee', assignee])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            issue_url = result.stdout.strip()
            return True, issue_url
        else:
            return False, result.stderr

    except Exception as e:
        return False, str(e)


def import_week(week_number, repo_owner, repo_name, dry_run=False):
    """Import tasks for a specific week"""

    data_dir = Path(__file__).parent.parent / 'data' / 'weeks'
    json_file = data_dir / f"week_{week_number:02d}.json"

    if not json_file.exists():
        print(f"❌ Week {week_number:02d} JSON not found: {json_file}")
        return 0, 0

    with open(json_file, 'r') as f:
        week_data = json.load(f)

    print(f"\n📋 Week {week_number:02d}: {week_data['phase']}")
    print(f"   Tasks: {len(week_data['tasks'])}")

    if dry_run:
        print("   (Dry run - no issues will be created)")
        return len(week_data['tasks']), 0

    success_count = 0
    fail_count = 0

    for i, task in enumerate(week_data['tasks'], 1):
        print(f"\n   [{i}/{len(week_data['tasks'])}] Creating: {task['id']} - {task['title'][:50]}...")

        success, result = create_issue_with_cli(repo_owner, repo_name, task, week_data)

        if success:
            print(f"      ✅ Created: {result}")
            success_count += 1
        else:
            print(f"      ❌ Failed: {result}")
            fail_count += 1

        # Rate limiting: sleep between requests
        if i < len(week_data['tasks']):
            sleep(2)  # 2 second delay between issues

    return success_count, fail_count


def import_all_tasks(repo_owner, repo_name, dry_run=False):
    """Import tasks from all weeks"""

    print("\n" + "=" * 60)
    print("IMPORTING TASKS TO GITHUB")
    print("=" * 60)
    print(f"Repository: {repo_owner}/{repo_name}")
    print("=" * 60)

    total_success = 0
    total_fail = 0

    for week in range(1, 13):
        success, fail = import_week(week, repo_owner, repo_name, dry_run)
        total_success += success
        total_fail += fail

    print("\n" + "=" * 60)
    print("IMPORT COMPLETE")
    print("=" * 60)
    print(f"✅ Successfully created: {total_success} issues")
    if total_fail > 0:
        print(f"❌ Failed: {total_fail} issues")
    print("=" * 60)

    return total_success, total_fail


def main():
    """Main execution"""
    parser = argparse.ArgumentParser(description='Import tasks from JSON to GitHub Issues')
    parser.add_argument('--week', '-w', type=int, help='Import specific week only (1-12)')
    parser.add_argument('--dry-run', '-d', action='store_true', help='Dry run (don\'t create issues)')

    args = parser.parse_args()

    # Get repository info
    repo_owner, repo_name = get_repo_info()

    if not repo_owner or not repo_name:
        print("❌ Repository information not available")
        print("\nPlease set environment variables:")
        print("   export REPO_OWNER='your-github-username'")
        print("   export REPO_NAME='your-repo-name'")
        return 1

    # Import tasks
    if args.week:
        if 1 <= args.week <= 12:
            success, fail = import_week(args.week, repo_owner, repo_name, args.dry_run)
        else:
            print("❌ Week must be between 1 and 12")
            return 1
    else:
        success, fail = import_all_tasks(repo_owner, repo_name, args.dry_run)

    if args.dry_run:
        print("\n✨ Dry run complete! Use without --dry-run to create issues.")
        return 0

    if fail == 0:
        print("\n✨ All tasks imported successfully!")
        return 0
    else:
        print(f"\n⚠️  Import completed with {fail} failures")
        return 1


if __name__ == "__main__":
    exit(main())
