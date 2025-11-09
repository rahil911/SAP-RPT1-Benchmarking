# Content Files - Agent 1 (Content Generator)

**Agent**: Agent 1 - Content Generator (RAG-Powered)
**Status**: ⏳ Awaiting Deployment
**Dependencies**:
- ✅ Research files complete (research/)
- ✅ Stakeholder intelligence complete (stakeholders/)
- ⏳ shared-data.json created by Research Agent
**Execution Mode**: Sequential (MUST wait for shared-data.json)

---

## 🎯 Agent 1 Mission

Create **7 high-quality markdown content files** using RAG (Retrieval-Augmented Generation) from research artifacts and Knowledge Graph API. These files form the core narrative of the SAP RPT-1 benchmarking proposal.

**Quality Target**: BCG/McKinsey consulting-grade content (9.5/10)
**Total Pages**: 40-50 pages across all files
**Key Requirement**: 100% team data from Knowledge Graph API (NO fabrication)

---

## 📋 Required Deliverables (7 Files)

### 1. sap-executive-summary-v1.md
**Target Length**: 2 pages
**Purpose**: High-level overview for executives

**Required Sections**:
- Project title and team
- Problem statement (1 paragraph)
- Solution approach (1 paragraph)
- Team qualifications (1 paragraph with match scores)
- Expected outcomes (1 paragraph)
- Timeline (12 weeks, key milestones)
- Budget (3 scenarios)

**Content Sources**:
- research/sap-company-intelligence.md
- research/team-matching.md
- project-requirements.json
- shared-data.json (team data)

**Quality Checks**:
- [ ] BCG/McKinsey caliber writing
- [ ] No jargon (executive-friendly)
- [ ] Quantified claims (X datasets, Y% match scores)
- [ ] 2 pages exactly

---

### 2. sap-problem-statement-v1.md
**Target Length**: 5-7 pages
**Purpose**: Articulate research gap using SCR framework

**Required Sections**:

**SITUATION** (Current State):
- SAP RPT-1 launched November 2025
- Claims to be "first enterprise relational foundation model"
- Promises zero-shot prediction on tabular data
- Market context: $XB tabular AI market, X% CAGR

**COMPLICATION** (The Problem):
- No independent, comprehensive benchmarking exists
- SAP's claims unvalidated by third parties
- Unclear when RPT-1 excels vs. traditional ML
- Enterprises lack evidence for adoption decisions
- Academic community needs rigorous evaluation

**RESOLUTION** (Our Solution):
- UW MSIM team conducts publication-quality benchmarking
- 70+ datasets, 7 models, statistical rigor
- NeurIPS/ICML submission target
- Provides SAP validation + practical guidance

**Content Sources**:
- research/sap-rpt-technical-deep-dive.md
- research/tabular-ml-landscape.md
- research/benchmarking-methodology.md
- project-requirements.json (research questions)

**Quality Checks**:
- [ ] SCR framework applied correctly
- [ ] Market sizing quantified with sources
- [ ] Research questions clearly stated
- [ ] Compelling narrative flow

---

### 3. sap-methodology-v1.md
**Target Length**: 8-12 pages
**Purpose**: Detailed benchmarking methodology

**Required Sections**:

**Three-Pillar Approach**:

**Pillar 1: Models**
- Foundation models: SAP RPT-1, TabPFN, TabICL
- AutoML: AutoGluon
- Baselines: CatBoost, XGBoost, LightGBM
- Configurations for each (lightweight, standard, full)

**Pillar 2: Datasets**
- TabArena 51 datasets (living benchmark)
- TabZilla 20 datasets (hardest subset)
- OpenML-CC18 subset (optional)
- Dataset characteristics and diversity

**Pillar 3: Evaluation**
- Metrics: ROC-AUC, Accuracy, F1, R², Runtime, Cost
- Statistical rigor: Friedman test, Nemenyi post-hoc
- Reproducibility: Docker, frozen environments
- Publication standards: NeurIPS/ICML compliance

**Timeline Breakdown**:
- Phase 0-5 with week-by-week tasks
- Milestones and deliverables per phase

**Content Sources**:
- research/benchmarking-methodology.md
- research/datasets-benchmarks.md
- research/compute-resources-guide.md
- project-requirements.json (experimental protocol)

**Quality Checks**:
- [ ] Three-pillar structure clear
- [ ] Statistical protocols detailed
- [ ] Reproducibility checklist included
- [ ] Timeline realistic and detailed

---

### 4. sap-team-presentation-v1.md (RAG-HEAVY)
**Target Length**: 6-8 pages
**Purpose**: Showcase team qualifications with 100% KG data

**CRITICAL**: This file is **100% RAG-powered**. ALL team data MUST come from Knowledge Graph API. NO fabrication.

**Required Sections**:

**Team Overview**:
- 4 UW MSIM students
- 14+ combined years of experience
- Fortune 500 backgrounds (SAP, AWS, Morgan Stanley, Rocket Mortgage)
- Combined GPA: 3.88-3.9/4.0

**Individual Profiles** (1.5 pages each):

**Profile Template**:
```markdown
### [Name from KG] - [Title from KG]
**Role**: [Role for this project]
**Match Score**: [X]% (from team-matching.md)

**Background**:
- Education: [Degree, University, GPA from KG]
- Experience: [X years from KG]
- Past Companies: [Exact names from KG with roles]

**Expertise Applied to This Project**:
- [Skill 1 from KG]: [How it applies]
- [Skill 2 from KG]: [How it applies]
- [Skill 3 from KG]: [How it applies]

**Key Achievements** (Quantified from KG):
1. [Achievement 1 with metric: "35% reduction in..."]
2. [Achievement 2 with metric: "$1M cost savings..."]
3. [Achievement 3 with metric: "90% model accuracy..."]

**Responsibilities for SAP RPT-1 Project**:
- [Primary responsibility 1]
- [Primary responsibility 2]
- [Primary responsibility 3]
```

**Data Sources** (RAG Workflow):
1. Query Knowledge Graph API: `/api/graph`
2. Extract from `shared-data.json['team']`
3. Validate against `research/team-matching.md`
4. Cross-reference `research/kg-data-cache.json`

**MANDATORY Team Member IDs** (from INTEGRATION_CONTRACT.md):
- Rahil M. Harihar (exact spelling, match score: 94%)
- Siddarth Bhave (exact spelling, match score: 92%)
- Mathew Jerry Meleth (exact spelling, match score: 88%)
- Shreyas B Subramanya (exact spelling, match score: 86%)

**Quality Checks** (CRITICAL):
- [ ] All names match KG exactly (spelling, middle initials)
- [ ] Match scores from team-matching.md
- [ ] All achievements have quantified metrics
- [ ] Skills list matches KG API
- [ ] Past companies exact names from KG
- [ ] Education includes GPAs from KG
- [ ] NO fabricated or hallucinated data
- [ ] Every claim verifiable in KG

---

### 5. sap-timeline-milestones-v1.md
**Target Length**: 5-7 pages
**Purpose**: Detailed 12-week timeline

**Required Sections**:

**Phase-by-Phase Breakdown**:

**Phase 0: Research & Intelligence** (Weeks 1-2)
- Tasks: [8 research tasks]
- Deliverables: [Research files, stakeholder intelligence]
- Milestone: Complete research foundation

**Phase 1: Content Generation** (Week 3)
- Tasks: [Agent 1 tasks]
- Deliverables: [7 content files + Word docs]
- Milestone: Content complete and validated

**Phase 2: Visual & Interactive** (Week 3, Parallel)
- Tasks: [Agent 2 & 3 tasks]
- Deliverables: [21 visual assets, 5 interactive elements]
- Milestone: All visuals and interactive complete

**Phase 3: Code Repository** (Weeks 2-4)
- Tasks: [Agent 4 tasks]
- Deliverables: [Benchmarking codebase]
- Milestone: Code repository ready

**Phase 4: GitHub Projects** (Week 4)
- Tasks: [Agent 5 tasks]
- Deliverables: [150+ tasks, timeline export]
- Milestone: Project management ready

**Phase 5: Final Assembly** (Week 4)
- Tasks: [Integration, validation, PPT, PDF]
- Deliverables: [Final presentations]
- Milestone: Proposal phase complete

**Phases 6-12: Execution** (Weeks 5-12)
- Brief overview of benchmarking execution
- Analysis and paper writing timeline

**Gantt Chart Format**:
- Week-by-week breakdown
- Dependencies clearly marked
- Critical path highlighted

**Content Sources**:
- project-requirements.json (timeline object)
- INTEGRATION_CONTRACT.md (agent coordination)
- shared-data.json (team assignments)

**Quality Checks**:
- [ ] 12 weeks detailed
- [ ] Dependencies noted
- [ ] Milestones clear
- [ ] Gantt-compatible format
- [ ] Realistic estimates

---

### 6. sap-expected-outcomes-v1.md
**Target Length**: 5-7 pages
**Purpose**: Define expected results and impact

**Required Sections**:

**Expected Findings**:
- Where SAP RPT-1 will likely excel (semantic-rich datasets)
- Where traditional ML may outperform (large datasets)
- Efficiency trade-offs (runtime vs. accuracy)
- Use case recommendations

**ROI for SAP**:
- **Market Credibility**: Independent academic validation (value: $50K+ consulting equivalent)
- **Competitive Intelligence**: How RPT-1 stacks up vs. TabPFN, TabICL
- **Use Case Clarity**: Data-driven positioning guidance
- **Feature Roadmap**: Optimization opportunities identified
- **Publication Impact**: Citable research for sales/marketing

**Academic Impact**:
- **Publication Venue**: NeurIPS 2026 or ICML 2026
- **Contribution**: First comprehensive independent RPT-1 benchmark
- **Citations**: Expected impact factor
- **Reproducibility**: Open-source code benefits community

**Practical Guidance for Enterprises**:
- Decision framework: When to use RPT-1 vs. AutoML vs. traditional ML
- Cost-benefit analysis by use case
- Implementation considerations

**Long-Term Collaboration**:
- Potential co-authorship with SAP researchers
- Access to domain-specific datasets
- Ongoing UW-SAP partnership

**Content Sources**:
- research/sap-rpt-technical-deep-dive.md (model capabilities)
- research/tabular-ml-landscape.md (competitive positioning)
- stakeholders/value-propositions-by-role.md (SAP value)
- project-requirements.json (success criteria)

**Quality Checks**:
- [ ] Expected findings realistic (not overpromising)
- [ ] ROI quantified where possible
- [ ] Academic impact clear
- [ ] Practical guidance actionable

---

### 7. sap-stakeholder-strategy-v1.md
**Target Length**: 5-7 pages
**Purpose**: Outreach strategy and stakeholder engagement

**Required Sections**:

**Key Stakeholders Identified**:
- Tier 1: Walter Sun, Sam Thelin, Johannes Hoffart
- Tier 2: Marco Spinaci, Markus Kohler, Maximilian Schambach
- Tier 3: Additional contacts

**Outreach Timeline**:
- Week 3: Initial contact (Tier 1)
- Week 4: Follow-up + Tier 2 expansion
- Week 5: Informational interviews
- Weeks 6-12: Ongoing engagement

**Value Propositions by Role**:
- Executive Leadership: Market credibility
- Core Researchers: Citation and validation
- Product Managers: Competitive intelligence
- Academic Liaisons: University partnership

**Engagement Strategy**:
- Email templates overview
- LinkedIn approach
- Meeting agendas
- Progress updates

**Collaboration Opportunities**:
- Data access (if applicable)
- Technical guidance
- Co-authorship potential
- Long-term partnership

**Content Sources**:
- stakeholders/sap-organizational-structure.md
- stakeholders/sap-rpt1-product-team.md
- stakeholders/value-propositions-by-role.md
- stakeholders/outreach-playbook.md

**Quality Checks**:
- [ ] Stakeholder mapping clear
- [ ] Timeline realistic
- [ ] Value propositions tailored
- [ ] Professional tone maintained

---

## 🔄 RAG Workflow (MANDATORY)

### Step 1: Wait for Dependencies

```python
# Agent 1 MUST wait for shared-data.json
import os, time, json

def wait_for_shared_data(timeout=300):
    start = time.time()
    while not os.path.exists("shared-data.json"):
        if time.time() - start > timeout:
            raise TimeoutError("shared-data.json not found")
        time.sleep(5)

    # Validate JSON
    with open("shared-data.json") as f:
        data = json.load(f)

    required_keys = ["team", "project", "research_highlights", "stakeholders"]
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing key: {key}")

    return data
```

### Step 2: Query Knowledge Graph API

```python
import requests

def fetch_team_data_from_kg():
    """
    Query Knowledge Graph API for fresh team data
    """
    KG_API_URL = "https://kg-student-backend.ambitiouswave-220155c4.eastus2.azurecontainerapps.io/api/graph"

    try:
        response = requests.get(KG_API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        # Fallback to cache
        print(f"KG API failed: {e}. Using cache.")
        with open("research/kg-data-cache.json") as f:
            return json.load(f)
```

### Step 3: Extract Team Context

```python
def extract_team_member_context(kg_data, member_id):
    """
    Extract specific member data for RAG
    """
    for member in kg_data['team']['members']:
        if member['id'] == member_id:
            return {
                "name": member['name'],  # EXACT spelling
                "title": member['title'],
                "skills": member['core_skills'],
                "achievements": member['key_achievements'],
                "experience": member['years_of_experience'],
                "past_companies": member['past_companies'],
                "education": member['education']
            }
    raise ValueError(f"Member {member_id} not found in KG data")
```

### Step 4: Generate Content with RAG

```python
def generate_team_presentation():
    """
    Example RAG workflow for team presentation
    """
    # 1. Load data
    shared_data = wait_for_shared_data()
    kg_data = fetch_team_data_from_kg()

    # 2. Extract context for each member
    team_profiles = []
    for member_id in ["member_1", "member_2", "member_3", "member_4"]:
        context = extract_team_member_context(kg_data, member_id)
        match_score = shared_data['team'][member_id]['match_score']

        # 3. Generate profile using context
        profile = f"""
### {context['name']} - {context['title']}
**Role**: {shared_data['team'][member_id]['role']}
**Match Score**: {match_score}%

**Background**:
- Education: {context['education']}
- Experience: {context['experience']} years
- Past Companies: {', '.join(context['past_companies'])}

**Expertise Applied**:
{format_skills(context['skills'])}

**Key Achievements**:
{format_achievements(context['achievements'])}
"""
        team_profiles.append(profile)

    return "\n\n".join(team_profiles)
```

---

## 📦 Output Deliverables

### Markdown Files (7 files in /content/)
1. sap-executive-summary-v1.md
2. sap-problem-statement-v1.md
3. sap-methodology-v1.md
4. sap-team-presentation-v1.md
5. sap-timeline-milestones-v1.md
6. sap-expected-outcomes-v1.md
7. sap-stakeholder-strategy-v1.md

### Word Documents (7 files in /content/DOCS/)
Convert all markdown files to .docx using:
- python-docx or pandoc
- Apply design system (Helvetica Neue, colors)
- Professional formatting

### Validation Checklist

Before completing, Agent 1 MUST verify:
- [ ] All 7 markdown files created
- [ ] All 7 Word documents created
- [ ] File naming follows convention (sap-{type}-v1.{ext})
- [ ] All team names match KG exactly
- [ ] All achievements have quantified metrics
- [ ] Design system colors referenced
- [ ] No fabricated data
- [ ] Cross-references valid
- [ ] Total 40-50 pages achieved
- [ ] BCG/McKinsey quality (9.5/10)

---

## 🚨 Critical Success Factors

### Must-Do
- ✅ Wait for shared-data.json before starting
- ✅ Query Knowledge Graph API for team data
- ✅ Use EXACT team member names from KG
- ✅ Include quantified metrics in all achievements
- ✅ Apply SCR framework to problem statement
- ✅ Three-pillar structure for methodology
- ✅ Cross-reference research files extensively

### Must-NOT-Do
- ❌ Start before shared-data.json exists
- ❌ Fabricate or hallucinate team data
- ❌ Misspell team member names
- ❌ Use vague achievements ("improved performance" vs. "35% improvement")
- ❌ Skip Word document conversion
- ❌ Violate file naming conventions

---

## 📊 Quality Standards

**Content Quality**: BCG/McKinsey caliber (9.5/10)
**Data Accuracy**: 100% (all team data from KG API)
**Citation Coverage**: 100% (all claims sourced)
**Design Compliance**: 100% (colors, fonts, white space)
**Total Pages**: 40-50 pages
**Timeline**: Complete in 1 day (15-20 hours)

---

**Status**: ⏳ Awaiting shared-data.json creation
**Owner**: Agent 1 (Content Generator)
**Next Step**: Research Agent creates shared-data.json → Agent 1 deploys
**Downstream**: Agent 2 & Agent 3 wait for these content files
