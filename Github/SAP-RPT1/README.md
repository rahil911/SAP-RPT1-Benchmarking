# GitHub Projects Automation

**Project Management Tools and Scripts**

This directory contains automation scripts for managing the SAP RPT-1 project using GitHub Projects (beta).

---

## Overview

These tools enable automated project management with:
- 150+ tasks across 12-week timeline
- GitHub Projects board integration
- Excel Gantt chart generation
- Task status tracking and updates

---

## Contents

### Configuration
**[config/github_config.py](config/github_config.py)**
- Centralized configuration management
- GitHub API credentials and endpoints
- Project settings and field definitions

### Automation Scripts
**[scripts/](scripts/)**

1. **setup_github_project.py**
   - Creates GitHub Projects v2 board
   - Defines custom fields (priority, estimated_hours, status)
   - Sets up project views and layouts

2. **import_tasks_to_github.py**
   - Imports tasks from JSON files to GitHub Projects
   - Creates issues and adds to project board
   - Assigns team members and sets metadata

3. **update_project_status.py**
   - Updates task status and progress
   - Modifies custom field values
   - Logs changes for audit trail

4. **create_timeline_excel.py**
   - Generates Excel Gantt chart from project data
   - Exports timeline visualization
   - Formats for presentation use

5. **full_automated_setup.py**
   - End-to-end automation orchestrator
   - Runs all setup scripts in sequence
   - Validates configuration and dependencies

### Utility Libraries
**[utils/](utils/)**

1. **github_api.py**
   - GitHub GraphQL API v4 wrapper
   - Rate limiting and error handling
   - Reusable query/mutation functions

2. **rate_limiter.py**
   - Token bucket rate limiting algorithm
   - Exponential backoff for retries
   - GitHub API quota management

---

## Setup Instructions

### Prerequisites
- GitHub personal access token with `repo` and `project` scopes
- Python 3.8+
- Dependencies: `requests`, `python-dotenv`, `openpyxl`

### Configuration
1. Copy `.env.template` to `.env` (not in repo - create locally)
2. Add your GitHub credentials:
   ```
   GITHUB_TOKEN=your_token_here
   GITHUB_REPO_OWNER=your_username
   GITHUB_REPO_NAME=SAP-RPT1-Benchmarking
   GITHUB_PROJECT_NUMBER=1
   ```

### Usage

**Full Setup** (recommended):
```bash
python scripts/full_automated_setup.py
```

**Individual Scripts**:
```bash
# Create project board
python scripts/setup_github_project.py

# Import tasks
python scripts/import_tasks_to_github.py

# Generate Excel timeline
python scripts/create_timeline_excel.py
```

---

## Project Structure

The automation manages:
- **150 tasks** across 12 weeks
- **7 milestones** (one per major phase)
- **4 team members** with role assignments
- **4 priority levels** (Critical, High, Medium, Low)
- **5 task statuses** (Todo, In Progress, Done, Blocked, Deferred)

---

## Features

### GitHub Projects Integration
- Automated board creation and configuration
- Custom fields for project metadata
- Issue-based task management
- Team member assignments

### Excel Timeline
- Gantt chart visualization
- Color-coded by priority
- Milestone markers
- Duration and dependencies

### Progress Tracking
- Status updates via API
- Completion percentage calculation
- Automated notifications
- Audit logging

---

## Documentation

For detailed automation guide, see:
- [GITHUB_PROJECTS_README.md](GITHUB_PROJECTS_README.md)

---

## Notes

- Task JSON files are stored locally (not in repository)
- GitHub Projects board is created on-demand
- Excel timelines generated as deliverables
- Scripts support both setup and ongoing management

---

**Prepared by**: University of Washington MSIM Team
**Last Updated**: November 2025
