# SAP RPT-1 GitHub Projects Automation

**Complete GitHub Projects management system for the SAP RPT-1 Benchmarking capstone project**

---

## 📋 Overview

This directory contains a complete GitHub Projects automation system for managing the 12-week SAP RPT-1 benchmarking capstone project. The system includes:

- **150 tasks** across **12 weeks**
- **7 major milestones** (M1-M7)
- **4 team members** with expertise-based assignments
- **Automated GitHub integration** (issue creation, project boards)
- **Excel Gantt chart** generation
- **Professional task tracking** at BCG/McKinsey quality level

---

## 🗂️ Directory Structure

```
SAP-RPT1/
├── data/
│   └── weeks/
│       ├── week_01.json  (15 tasks - Research & Planning)
│       ├── week_02.json  (15 tasks - Research & Planning)
│       ├── week_03.json  (13 tasks - Proposal Development)
│       ├── week_04.json  (15 tasks - Proposal Development)
│       ├── week_05.json  (15 tasks - Infrastructure & Dataset Prep)
│       ├── week_06.json  (10 tasks - Benchmarking Experiments)
│       ├── week_07.json  (9 tasks - Benchmarking Experiments)
│       ├── week_08.json  (10 tasks - Benchmarking Experiments)
│       ├── week_09.json  (10 tasks - Benchmarking Experiments)
│       ├── week_10.json  (11 tasks - Analysis & Insights)
│       ├── week_11.json  (12 tasks - Analysis & Insights)
│       └── week_12.json  (15 tasks - Documentation & Presentation)
│
├── scripts/
│   ├── full_automated_setup.py       (🚀 Main automation script)
│   ├── create_timeline_excel.py      (📊 Excel Gantt chart generator)
│   ├── setup_github_project.py       (Create GitHub Project board)
│   ├── import_tasks_to_github.py     (Import tasks as GitHub Issues)
│   ├── add_custom_fields.py          (Add custom fields to project)
│   └── update_project_status.py      (Track task progress)
│
├── config/
│   └── github_config.py               (API configuration)
│
├── utils/
│   ├── github_api.py                  (GitHub API wrapper)
│   └── rate_limiter.py                (API rate limiting)
│
├── deliverables/
│   └── sap-project-timeline.xlsx      (Excel timeline - auto-generated)
│
├── logs/
│   └── import_log.txt                 (Execution logs)
│
├── .env.template                      (Environment variables template)
├── README.md                          (Main documentation)
└── GITHUB_PROJECTS_README.md         (This file)
```

---

## 🚀 Quick Start

### Option 1: Generate Excel Timeline Only (No GitHub Required)

```bash
# Navigate to scripts directory
cd /Users/rahilharihar/TBD-Sponsers/SAP/Github/SAP-RPT1/scripts

# Install dependencies
pip install pandas xlsxwriter

# Generate Excel timeline
python3 create_timeline_excel.py

# Output: ../deliverables/sap-project-timeline.xlsx
```

### Option 2: Full GitHub Automation (Requires GitHub Access)

```bash
# 1. Set up environment variables
cp .env.template .env
# Edit .env with your GitHub token and repository info

# 2. Install dependencies
pip install pandas xlsxwriter requests

# 3. Install GitHub CLI (recommended)
# macOS: brew install gh
# Linux: See https://cli.github.com/
# Windows: See https://cli.github.com/

# 4. Authenticate GitHub CLI
gh auth login

# 5. Run full automation
python3 scripts/full_automated_setup.py
```

---

## 📊 Task Breakdown

| Week | Phase | Tasks | Key Deliverables |
|------|-------|-------|------------------|
| 1 | Research & Planning | 15 | Company intelligence, technical deep dive, stakeholder mapping |
| 2 | Research & Planning | 15 | Model analysis, dataset strategy, metrics framework |
| 3 | Proposal Development | 13 | Content sections, competitive analysis, methodology |
| 4 | Proposal Development | 15 | PowerPoint, PDF reports, HTML viewer, QR codes |
| 5 | Infrastructure & Dataset Prep | 15 | Model wrappers, Docker containers, dataset downloads |
| 6 | Benchmarking Experiments | 10 | Baseline experiments (XGBoost, CatBoost, LightGBM, AutoGluon) |
| 7 | Benchmarking Experiments | 9 | Foundation model experiments (TabPFN, TabICL, SAP RPT-1) |
| 8 | Benchmarking Experiments | 10 | Validation, performance analysis, visualizations |
| 9 | Benchmarking Experiments | 10 | Statistical testing (Friedman, Nemenyi, Wilcoxon) |
| 10 | Analysis & Insights | 11 | Key insights, use case recommendations, executive summary |
| 11 | Analysis & Insights | 12 | NeurIPS/ICML paper drafting (all sections) |
| 12 | Documentation & Presentation | 15 | Paper finalization, code release, SAP presentation, retrospective |

**TOTAL: 150 tasks**

---

## 👥 Team Assignments

Tasks are distributed based on team member expertise:

| Team Member | Primary Role | Task Count (Est.) | Key Responsibilities |
|-------------|--------------|-------------------|----------------------|
| **Rahil M. Harihar** | Product Lead & AI/ML Strategy | ~40 tasks | Project leadership, stakeholder management, executive content, product strategy |
| **Siddarth Bhave** | Technical Lead & AI/ML Engineering | ~45 tasks | Software architecture, model wrappers, benchmarking code, paper methodology |
| **Mathew Jerry Meleth** | Data Engineering & Cloud Infrastructure | ~35 tasks | Dataset management, cloud setup, data pipelines, infrastructure |
| **Shreyas B Subramanya** | Operations & Analytics Lead | ~30 tasks | Statistical analysis, dashboards, documentation, QA, weekly reports |

*Note: Task counts are approximate and may overlap for collaborative tasks*

---

## 🎯 7 Major Milestones

| Milestone | Week | Due Date | Description |
|-----------|------|----------|-------------|
| **M1: Research Foundation Complete** | 2 | Nov 22, 2025 | All research files and stakeholder intelligence completed |
| **M2: Proposal Content Complete** | 3 | Nov 29, 2025 | All content files (markdown and Word) completed |
| **M3: Visuals & Interactive Complete** | 3 | Nov 29, 2025 | All visual assets and interactive elements completed |
| **M4: Proposal Delivered to SAP** | 4 | Dec 6, 2025 | Final deliverables (PPT, PDF, HTML) delivered |
| **M5: Benchmarking Complete** | 9 | Jan 17, 2026 | All experimental runs completed across 70+ datasets |
| **M6: Statistical Analysis Complete** | 10 | Jan 24, 2026 | Friedman/Nemenyi tests, critical difference diagrams completed |
| **M7: Paper Draft Complete** | 12 | Jan 31, 2026 | NeurIPS/ICML paper draft ready for submission |

---

## 📖 Task JSON Schema

Each `week_XX.json` file follows this structure:

```json
{
  "week": 1,
  "phase": "Research & Planning",
  "start_date": "2025-11-08",
  "end_date": "2025-11-14",
  "tasks": [
    {
      "id": "W01-T01",
      "title": "Task title",
      "description": "Detailed task description with deliverable info",
      "owner": "Team Member Name",
      "estimated_hours": 8,
      "priority": "Critical",
      "deliverable": "path/to/deliverable.md",
      "dependencies": ["W01-T02", "W01-T03"],
      "tools": ["WebSearch", "Write", "Bash"],
      "success_criteria": "Clear criteria for task completion"
    }
  ]
}
```

### Task Priority Levels

- **Critical**: Must complete on time, blocks other work
- **High**: Important but some flexibility
- **Medium**: Standard priority
- **Low**: Nice to have, can be deferred if needed

---

## 🔧 Automation Scripts

### 1. **full_automated_setup.py** (Master Script)

End-to-end automation that orchestrates all other scripts.

```bash
python3 scripts/full_automated_setup.py
```

**What it does:**
1. Creates GitHub Project board
2. Adds custom fields (Priority, Hours, Deliverable, Week)
3. Creates 7 milestones
4. Imports all 150 tasks as GitHub Issues
5. Generates Excel timeline

### 2. **create_timeline_excel.py** (Excel Generator)

Generates professional Excel Gantt chart with all tasks.

```bash
python3 scripts/create_timeline_excel.py --output custom_name.xlsx
```

**Output sheets:**
- Timeline (all 150 tasks with metadata)
- Summary (project overview)
- Phase Breakdown (tasks by phase)
- Owner Breakdown (tasks by team member)

### 3. **setup_github_project.py** (Project Creator)

Creates GitHub Project (v2) board.

```bash
python3 scripts/setup_github_project.py
```

**Requires:**
- GitHub CLI (`gh`) or
- `GITHUB_TOKEN` environment variable

### 4. **import_tasks_to_github.py** (Task Importer)

Imports tasks from JSON files to GitHub Issues.

```bash
# Import all weeks
python3 scripts/import_tasks_to_github.py

# Import specific week
python3 scripts/import_tasks_to_github.py --week 1

# Dry run (preview without creating)
python3 scripts/import_tasks_to_github.py --dry-run
```

**Features:**
- Creates issues with task metadata
- Adds labels (phase, priority, week)
- Assigns team members
- Includes dependencies and success criteria
- Rate limiting (2 sec between issues)

---

## ⚙️ Configuration

### Environment Variables

Create `.env` file from template:

```bash
cp .env.template .env
```

Required variables:
```bash
GITHUB_TOKEN=your_token_here
REPO_OWNER=your-username
REPO_NAME=sap-rpt1-benchmarking
```

### GitHub CLI Authentication

```bash
# Login to GitHub
gh auth login

# Verify authentication
gh auth status

# Set default repository
gh repo set-default OWNER/REPO
```

---

## 📈 Excel Timeline Features

The generated Excel file includes:

✅ **Timeline Sheet**
- All 150 tasks with full metadata
- Color-coded priority levels
- Gantt-style date visualization
- Filterable columns

✅ **Summary Sheet**
- Total tasks: 150
- Total weeks: 12
- Total hours: ~600 (estimated)
- Project dates: Nov 8, 2025 - Jan 31, 2026

✅ **Phase Breakdown**
- Tasks per phase
- Hours per phase

✅ **Owner Breakdown**
- Tasks per team member
- Hours per team member

---

## 🔍 Task Statistics

### By Phase

| Phase | Weeks | Tasks | % of Total |
|-------|-------|-------|------------|
| Research & Planning | 1-2 | 30 | 20% |
| Proposal Development | 3-4 | 28 | 19% |
| Infrastructure & Dataset Prep | 5 | 15 | 10% |
| Benchmarking Experiments | 6-9 | 39 | 26% |
| Analysis & Insights | 10-11 | 23 | 15% |
| Documentation & Presentation | 12 | 15 | 10% |

### By Priority

| Priority | Count | % of Total |
|----------|-------|------------|
| Critical | ~45 | 30% |
| High | ~50 | 33% |
| Medium | ~40 | 27% |
| Low | ~15 | 10% |

---

## 🚨 Common Issues & Solutions

### Issue: "gh: command not found"

**Solution:**
```bash
# macOS
brew install gh

# Ubuntu/Debian
sudo apt install gh

# Or use API-based approach (see scripts)
```

### Issue: "GITHUB_TOKEN not set"

**Solution:**
1. Create token: https://github.com/settings/tokens
2. Add to `.env` file
3. Source environment: `source .env`

### Issue: "Rate limit exceeded"

**Solution:**
- Scripts include 2-second delays between API calls
- If needed, increase delay in `import_tasks_to_github.py`
- Use `--week` flag to import incrementally

### Issue: "Permission denied"

**Solution:**
- Check token scopes (need: `repo`, `project`)
- Verify repository access
- Re-authenticate GitHub CLI: `gh auth login`

---

## 📚 Additional Resources

### GitHub Documentation
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitHub CLI](https://cli.github.com/)
- [GraphQL API](https://docs.github.com/en/graphql)

### Python Dependencies
```bash
pip install pandas xlsxwriter requests python-dotenv
```

### UW MSIM Capstone Resources
- Project timeline aligns with UW capstone deadlines
- Deliverables meet academic quality standards
- Task breakdown suitable for 4-person team

---

## ✅ Validation Checklist

Before running automation:

- [ ] All 12 week JSON files present in `data/weeks/`
- [ ] Total 150 tasks confirmed
- [ ] GitHub token created and added to `.env`
- [ ] Repository owner and name configured
- [ ] GitHub CLI installed and authenticated (optional)
- [ ] Python dependencies installed
- [ ] Team member GitHub usernames verified

---

## 🎯 Success Metrics

Project management quality indicators:

✅ **Task Coverage**: 150+ tasks across all project phases
✅ **Team Balance**: Even distribution across 4 members
✅ **Time Estimates**: Realistic hours based on complexity
✅ **Dependencies**: Proper task sequencing and dependencies
✅ **Milestones**: 7 clear milestones aligned with deliverables
✅ **Documentation**: Every task has success criteria
✅ **Automation**: Full end-to-end GitHub integration

---

## 📞 Support

For issues or questions:

1. Check this README
2. Review contract: `AGENT_5_CONTRACT.md`
3. Examine example JSON: `data/weeks/week_01.json`
4. Review shared data: `../shared-data.json`

---

**Project**: SAP RPT-1 Benchmarking Study
**Team**: UW MSIM Capstone Team (4 members)
**Duration**: Nov 8, 2025 - Jan 31, 2026 (12 weeks)
**Quality Standard**: BCG/McKinsey level

**Agent**: Agent 5 (GitHub Projects Manager)
**Created**: November 8, 2025
**Version**: 1.0

---
