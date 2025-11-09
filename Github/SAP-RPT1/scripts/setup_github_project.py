#!/usr/bin/env python3
"""
setup_github_project.py
Create GitHub Project board using GitHub CLI or API

This script creates a new GitHub Project (v2) for tracking the SAP RPT-1
benchmarking project tasks.

Usage:
    python3 setup_github_project.py

Prerequisites:
    - GitHub CLI (gh) installed and authenticated, OR
    - GITHUB_TOKEN environment variable set

Author: Agent 5 (GitHub Projects Manager)
Date: 2025-11-08
"""

import os
import subprocess
import sys


def create_project_with_cli(name, description):
    """Create GitHub Project using GitHub CLI"""

    print(f"📦 Creating GitHub Project: {name}")
    print(f"   Description: {description}")

    try:
        # Check if gh CLI is installed
        result = subprocess.run(['gh', '--version'], capture_output=True, text=True)

        if result.returncode != 0:
            print("❌ GitHub CLI (gh) not installed")
            print("   Install: https://cli.github.com/")
            return None

        print("✅ GitHub CLI found")

        # Create project using gh CLI
        cmd = [
            'gh', 'project', 'create',
            '--title', name,
            '--body', description
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Project created successfully")
            # Extract project URL from output
            project_url = result.stdout.strip()
            print(f"   Project URL: {project_url}")

            # Extract project ID from URL (last segment)
            project_id = project_url.split('/')[-1] if project_url else None

            return project_id
        else:
            print(f"❌ Error creating project: {result.stderr}")
            return None

    except FileNotFoundError:
        print("❌ GitHub CLI (gh) not found in PATH")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return None


def create_project_with_api(name, description):
    """Create GitHub Project using GitHub GraphQL API"""

    print("🔧 Attempting to create project via GitHub API...")

    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ GITHUB_TOKEN not set in environment")
        return None

    try:
        import requests

        # Get organization or user ID first
        owner = os.getenv('REPO_OWNER')

        if not owner:
            print("❌ REPO_OWNER not set in environment")
            return None

        # GraphQL query to create project
        query = """
        mutation($ownerId: ID!, $title: String!, $body: String!) {
          createProjectV2(input: {ownerId: $ownerId, title: $title, body: $body}) {
            projectV2 {
              id
              url
              title
            }
          }
        }
        """

        # Note: This is a simplified example
        # In production, you'd need to:
        # 1. Get the owner's node ID first
        # 2. Handle authentication properly
        # 3. Add error handling

        print("⚠️  API-based project creation requires additional setup")
        print("   Please use GitHub CLI (gh) or create project manually")

        return None

    except ImportError:
        print("❌ 'requests' library not installed")
        print("   Install: pip install requests")
        return None
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None


def create_project(name="SAP RPT-1 Benchmarking", description="12-week capstone project"):
    """
    Create GitHub Project board

    Args:
        name: Project name
        description: Project description

    Returns:
        str: Project ID if successful, None otherwise
    """

    print("\n" + "=" * 60)
    print("CREATING GITHUB PROJECT")
    print("=" * 60)

    # Try GitHub CLI first (recommended)
    project_id = create_project_with_cli(name, description)

    if project_id:
        return project_id

    # Fallback to API if CLI fails
    print("\n⚠️  GitHub CLI method failed, trying API...")
    project_id = create_project_with_api(name, description)

    if project_id:
        return project_id

    # If both fail, provide instructions
    print("\n" + "=" * 60)
    print("❌ AUTOMATIC PROJECT CREATION FAILED")
    print("=" * 60)
    print("\n📖 Manual Setup Instructions:")
    print("   1. Go to: https://github.com/orgs/[YOUR_ORG]/projects")
    print("   2. Click 'New project'")
    print("   3. Choose 'Board' layout")
    print("   4. Name: 'SAP RPT-1 Benchmarking'")
    print("   5. Description: '12-week capstone project for SAP sponsor'")
    print("   6. Click 'Create project'")
    print("\n   Then, you can import tasks using import_tasks_to_github.py")
    print("=" * 60)

    return None


def main():
    """Main execution"""
    project_id = create_project()

    if project_id:
        print(f"\n✅ Success! Project ID: {project_id}")
        return 0
    else:
        print("\n⚠️  Project creation incomplete. See instructions above.")
        return 1


if __name__ == "__main__":
    exit(main())
