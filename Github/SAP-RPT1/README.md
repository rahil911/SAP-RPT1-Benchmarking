# GitHub Projects Management - Agent 5

**Agent**: Agent 5 - Project Manager
**Purpose**: Convert 12-week timeline into GitHub Projects dashboard
**Total Tasks**: 150+ tasks across 12 weeks
**Timeline**: Week 4 (after content creation)

---

## 🎯 Mission

Create a **GitHub Projects v2 board** with complete task breakdown, assignments, milestones, and tracking for the 12-week SAP RPT-1 benchmarking project.

---

## 📁 Structure

```
Github/SAP-RPT1/
├── README.md (this file)
├── AGENT_CONTRACT.md (JSON schema for week files)
│
├── data/
│   └── weeks/
│       ├── week_01.json (15-20 tasks)
│       ├── week_02.json
│       ├── ...
│       └── week_12.json
│
├── scripts/
│   ├── full_automated_setup.py (end-to-end automation)
│   ├── setup_github_project.py (create project board)
│   ├── import_tasks_to_github.py (bulk issue creation)
│   ├── add_custom_fields.py (priority, hours, etc.)
│   └── update_project_status.py (track progress)
│
├── config/
│   └── github_config.py (API credentials)
│
├── utils/
│   ├── github_api.py (GitHub API wrapper)
│   └── rate_limiter.py (avoid API limits)
│
├── logs/
│   └── import_log.txt
│
├── sap-project-timeline.xlsx (Excel Gantt chart)
└── .env (GitHub PAT token - gitignored)
```

---

## 📋 Task JSON Schema (AGENT_CONTRACT.md)

```json
{
  "week": 1,
  "phase": "Research & Intelligence",
  "tasks": [
    {
      "id": "W01-T01",
      "title": "SAP company intelligence research",
      "description": "Web research on SAP AI Foundation, RPT-1 product positioning, market context. Deliverable: sap-company-intelligence.md (30-40 pages).",
      "owner": "Rahil",
      "estimated_hours": 8,
      "priority": "Critical",
      "deliverable": "sap-company-intelligence.md",
      "dependencies": [],
      "tools": ["WebSearch", "WebFetch"],
      "success_criteria": "30+ pages, 20+ sources cited, all claims quantified"
    },
    ...
  ]
}
```

---

## 🚀 Automation Scripts

### full_automated_setup.py

```python
#!/usr/bin/env python3
"""
End-to-end automation: JSON → GitHub Projects
"""

import os
import json
from scripts.setup_github_project import create_project
from scripts.import_tasks_to_github import import_all_tasks
from scripts.add_custom_fields import setup_custom_fields

def main():
    # 1. Create GitHub Project
    project_id = create_project(
        name="SAP RPT-1 Benchmarking",
        description="12-week capstone project"
    )

    # 2. Add custom fields
    setup_custom_fields(project_id)

    # 3. Import tasks from JSON
    for week in range(1, 13):
        json_file = f"data/weeks/week_{week:02d}.json"
        if os.path.exists(json_file):
            import_all_tasks(json_file, project_id)

    print(f"✅ GitHub Project created: {project_id}")

if __name__ == "__main__":
    main()
```

---

## 📊 Excel Timeline Export

### create_timeline_excel.py

```python
import pandas as pd
from datetime import datetime, timedelta

def create_excel_timeline():
    """
    Generate Excel file with Gantt chart
    """
    start_date = datetime(2025, 11, 8)  # Project start

    tasks = []
    for week in range(1, 13):
        with open(f"data/weeks/week_{week:02d}.json") as f:
            week_data = json.load(f)

        for task in week_data['tasks']:
            task_start = start_date + timedelta(weeks=week-1)
            task_end = task_start + timedelta(days=7)

            tasks.append({
                'Week': week,
                'Task ID': task['id'],
                'Task': task['title'],
                'Owner': task['owner'],
                'Hours': task['estimated_hours'],
                'Priority': task['priority'],
                'Start': task_start,
                'End': task_end,
                'Deliverable': task['deliverable']
            })

    df = pd.DataFrame(tasks)
    df.to_excel('sap-project-timeline.xlsx', index=False)
```

---

## ✅ Deliverables

- [ ] 12 week JSON files created (week_01.json to week_12.json)
- [ ] AGENT_CONTRACT.md with JSON schema
- [ ] GitHub automation scripts (5 scripts)
- [ ] Excel timeline export
- [ ] GitHub Projects v2 board created
- [ ] 150+ tasks imported as issues
- [ ] Custom fields added (Priority, Hours, Deliverable)
- [ ] 7 milestones created (M1-M7)
- [ ] Team members assigned

---

## 📊 Milestones

1. **M1**: Research foundation complete (Week 2)
2. **M2**: Content & visuals complete (Week 3)
3. **M3**: Code repository ready (Week 4)
4. **M4**: Proposal delivered (Week 4)
5. **M5**: Benchmarking experiments complete (Week 10)
6. **M6**: Analysis & results (Week 11)
7. **M7**: Paper draft complete (Week 12)

---

**Status**: ⏳ Awaiting Agent 5 deployment
**Timeline**: Week 4 (after content creation)
**Total Tasks**: 150+ across 12 weeks
