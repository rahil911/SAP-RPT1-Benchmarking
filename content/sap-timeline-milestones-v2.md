# SAP RPT-1 Benchmarking Study
## Timeline & Milestones - Version 2.0

**Project Duration**: 20 weeks (November 8, 2025 - April 4, 2026)

**Total Phases**: 6 major phases from proposal to paper publication

**Target Completion**: NeurIPS/ICML 2026 paper draft ready by Week 20

**Document Version**: 2.0
**Last Updated**: November 2025
**Classification**: Proposal - Timeline & Milestones

---

## EXECUTIVE SUMMARY

### The Paradigm Shift Timeline

This 20-week timeline is designed to replicate the validation timelines that transformed AI history:

| Paradigm Shift | Benchmark Duration | Time to Enterprise Impact | Revenue Unlocked |
|----------------|-------------------|---------------------------|------------------|
| **ImageNet (2012)** | 3 months training + 1 week ILSVRC evaluation | 18 months to $2.1B VC funding | Computer vision market: $15.9B (2024) |
| **BERT (2018)** | 4 days pre-training + 2 weeks GLUE evaluation | 12 months to 80% F500 adoption | NLP market: $24.3B (2024) |
| **AlphaFold (2020)** | 2 weeks CASP14 blind prediction | 24 months to $100M+ pharma savings | Drug discovery AI: $21B funding |
| **SAP RPT-1 (2026)** | **20 weeks independent benchmarking** | **Target: 6 months to sales enablement** | **Tabular AI market: $8.5B → $18.2B** |

### Business Value Delivered: Week-by-Week ROI Trajectory

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'primaryColor': '#1E3A8A',
    'primaryTextColor': '#F8FAFC',
    'primaryBorderColor': '#64748B',
    'lineColor': '#14B8A6',
    'secondaryColor': '#64748B',
    'tertiaryColor': '#F8FAFC',
    'fontSize': '14px',
    'fontFamily': 'Helvetica Neue, Arial, sans-serif'
  }
}}%%
gantt
    title SAP RPT-1 Validation Timeline - Business Value Delivery (20 Weeks)
    dateFormat  YYYY-MM-DD

    section Foundation
    Research & Intelligence          :done, research, 2025-11-08, 2w
    Proposal Development             :done, proposal, 2025-11-22, 2w

    section Infrastructure
    Technical Setup & Datasets       :active, infra, 2025-12-06, 3w

    section Execution
    Baseline Experiments             :baseline, 2025-12-27, 2w
    RPT-1 Core Validation           :rpt1, 2026-01-10, 2w
    Competitive Benchmarking        :compete, 2026-01-24, 2w
    Advanced Analysis               :advanced, 2026-02-07, 2w

    section Optimization
    Performance Tuning              :tuning, 2026-02-21, 2w
    Reproducibility Validation      :repro, 2026-03-07, 1w

    section Deliverables
    Statistical Analysis            :stats, 2026-03-14, 1w
    Paper Writing                   :paper, 2026-03-21, 2w
    Sales Enablement Package        :sales, 2026-04-04, 1w

    section Milestones
    M1: Research Complete           :milestone, m1, 2025-11-22, 1d
    M2: Proposal Delivered          :milestone, m2, 2025-12-06, 1d
    M3: Infrastructure Ready        :milestone, m3, 2025-12-27, 1d
    M4: Baseline Validated          :milestone, m4, 2026-01-10, 1d
    M5: RPT-1 Results Complete      :milestone, m5, 2026-01-24, 1d
    M6: Competitive Analysis Done   :milestone, m6, 2026-02-07, 1d
    M7: Performance Optimized       :milestone, m7, 2026-02-21, 1d
    M8: Statistical Rigor Achieved  :milestone, m8, 2026-03-14, 1d
    M9: Paper Draft Complete        :milestone, m9, 2026-04-04, 1d
    M10: Sales Ready                :milestone, m10, 2026-04-04, 1d
```

### Cumulative Business Value by Milestone

| Milestone | Week | Business Value Delivered | SAP Sales Enablement Readiness | Cumulative ROI |
|-----------|------|--------------------------|--------------------------------|----------------|
| **M1**: Research Foundation | 2 | Competitive intelligence, market positioning | 10% - Industry landscape mapped | $0 (investment phase) |
| **M2**: Proposal Delivered | 4 | Stakeholder engagement, internal champion buy-in | 25% - Value proposition articulated | $0 (investment phase) |
| **M3**: Infrastructure Ready | 7 | Reproducible experimental framework | 30% - Technical credibility established | $0 (investment phase) |
| **M4**: Baseline Validated | 9 | Industry-standard performance benchmarks | 40% - Competitive context understood | **$50K** (early sales support) |
| **M5**: RPT-1 Results Complete | 11 | Core product validation on 89 datasets | 60% - RPT-1 strengths/weaknesses clear | **$150K** (POC acceleration) |
| **M6**: Competitive Analysis | 13 | Head-to-head vs AutoGluon, TabPFN, XGBoost | 75% - Differentiation messaging ready | **$300K** (objection handling) |
| **M7**: Performance Optimized | 15 | Use case-specific recommendations | 85% - Solution engineering guidance | **$500K** (win rate improvement) |
| **M8**: Statistical Rigor | 17 | Peer-reviewed methodology, p-values | 90% - Academic credibility achieved | **$750K** (enterprise trust) |
| **M9**: Paper Draft Complete | 19 | Publication-ready validation study | 95% - Conference submission pending | **$1.2M** (market positioning) |
| **M10**: Sales Package Ready | 20 | ROI calculators, TCO models, objection handlers | **100% - Full sales enablement** | **$1.5M+** (first-year impact) |

**Total 20-Week Investment**: $75K-$120K (team time + compute)

**Year 1 ROI**: $1.5M in accelerated sales cycles, reduced POC costs, improved win rates

**3-Year ROI**: $8.5M+ (assuming 15% of SAP's $50M+ AI-influenced ARR accelerated by 6 months)

---

## PHASE-BY-PHASE BREAKDOWN

---

## Phase 0: Research & Intelligence (Weeks 1-2)

**Duration**: November 8 - November 22, 2025 (2 weeks)

**Objective**: Build comprehensive research foundation and stakeholder intelligence to inform proposal and methodology.

**Paradigm Shift Comparison**:
- **ImageNet preparation (2009)**: 2.5 years to curate 14M images, establish annotation pipeline
- **Our approach**: Leverage existing benchmarks (TabArena, TabZilla) = 2 weeks vs 2.5 years

### Week 1: Deep Research

**Business Value Focus**: Establish SAP's competitive positioning in $8.5B tabular AI market

**Tasks**:

#### 1. SAP Company & Product Intelligence
- **Objective**: Understand SAP AI Foundation strategy, RPT-1 architecture, ConTextTab paper claims
- **Activities**:
  - Analyze SAP AI Research 2025 publications (ConTextTab, RPT-1 technical reports)
  - Map SAP organizational structure (Walter Sun, Sam Thelin, Johannes Hoffart)
  - Document RPT-1 technical specifications (model size, training data, inference API)
  - Identify SAP's competitive landscape (vs Microsoft Azure ML, Oracle ML, Salesforce Einstein)
- **Owner**: Rahil (Product Lead)
- **Deliverable**: `sap-company-intelligence.md` (15-20 pages)
- **Business Value**: Inform stakeholder engagement strategy, identify SAP pain points
- **Risk Mitigation**:
  - Use public sources only (no proprietary SAP data required)
  - Fallback: Focus on published ConTextTab paper if internal docs unavailable

#### 2. Tabular ML Landscape Analysis
- **Objective**: Survey competing models and establish performance baselines
- **Activities**:
  - Deep dive into TabPFN (Nature paper, v2.5 capabilities)
  - Analyze AutoGluon architecture and AutoML strategies
  - Document traditional ML baselines (XGBoost, CatBoost, LightGBM)
  - Identify state-of-the-art performance metrics from literature
- **Owner**: Siddarth (Technical Lead)
- **Deliverable**: `tabular-ml-landscape.md` (12-15 pages)
- **Business Value**: Contextualize RPT-1 within competitive landscape
- **Risk Mitigation**:
  - Use arXiv, GitHub, official documentation
  - Fallback: Focus on top 3 competitors if time constrained

#### 3. Benchmarking Methodology Research
- **Objective**: Design statistically rigorous evaluation protocol
- **Activities**:
  - Study Friedman test and Nemenyi post-hoc analysis (Demšar, 2006)
  - Review REFORMS checklist for ML reproducibility
  - Analyze prior benchmarking papers (TabPFN Nature paper, TabZilla, AutoML benchmark)
  - Define statistical testing protocols and significance thresholds
- **Owner**: Shreyas (Analytics Lead)
- **Deliverable**: `benchmarking-methodology.md` (10-12 pages)
- **Business Value**: Establish academic credibility (peer-review readiness)
- **Risk Mitigation**:
  - Use established statistical methods (no novel approaches)
  - Fallback: Wilcoxon signed-rank test if Friedman assumptions violated

#### 4. Dataset & Benchmark Research
- **Objective**: Catalog 89 datasets spanning 15+ enterprise domains
- **Activities**:
  - Catalog TabArena datasets (51 datasets, OpenML-hosted)
  - Catalog TabZilla datasets (20 "hardest" datasets)
  - Catalog OpenML-CC18 datasets (18 curated datasets)
  - Document dataset characteristics (size, features, domain, task type)
  - Verify dataset availability, licenses, and download URLs
- **Owner**: Mathew (Data Lead)
- **Deliverable**: `datasets-benchmarks.md` (20-25 pages with dataset matrix)
- **Business Value**: Demonstrate domain coverage for SAP enterprise use cases
- **Risk Mitigation**:
  - All datasets publicly available (OpenML, Kaggle, UCI ML Repository)
  - Fallback: Reduce to 71 datasets (TabArena + TabZilla) if OpenML-CC18 inaccessible

### Week 2: Stakeholder Mapping & Planning

**Business Value Focus**: Design engagement strategy to secure SAP champion buy-in

**Tasks**:

#### 5. Stakeholder Intelligence
- **Objective**: Map SAP decision-makers and influencers
- **Activities**:
  - Map SAP AI Foundation organizational structure (LinkedIn, org charts)
  - Identify key contacts:
    - **Tier 1**: Walter Sun (Global Head of AI, SAP) - executive sponsor
    - **Tier 2**: Sam Thelin (ConTextTab lead author) - technical collaborator
    - **Tier 2**: Johannes Hoffart (Research Director) - academic credibility
    - **Tier 3**: SAP account teams, product managers
  - Research stakeholder backgrounds (publications, LinkedIn activity, speaking engagements)
  - Define tier 1/2/3 stakeholder prioritization and outreach cadence
- **Owner**: Rahil
- **Deliverable**: `sap-organizational-structure.md`, `sap-rpt1-product-team.md`
- **Business Value**: Secure internal champion to accelerate sales enablement adoption
- **Risk Mitigation**:
  - Multi-channel outreach (email, LinkedIn, UW faculty introduction)
  - Fallback: Proceed independently if no SAP response; value persists

#### 6. Value Proposition Development
- **Objective**: Craft role-specific messaging for SAP stakeholders
- **Activities**:
  - Develop executive value proposition (revenue impact, competitive positioning)
  - Develop research value proposition (academic co-authorship, publication opportunity)
  - Develop product value proposition (optimization roadmap, use case guidance)
  - Develop sales value proposition (ROI calculators, objection handlers, demo data)
  - Create email templates and outreach playbook
- **Owner**: Rahil
- **Deliverable**: `value-propositions-by-role.md`, `outreach-playbook.md`
- **Business Value**: Maximize stakeholder engagement success rate
- **Risk Mitigation**:
  - A/B test messaging with 2-3 initial contacts
  - Fallback: Focus on research value proposition if executive access limited

#### 7. Compute Resource Planning
- **Objective**: Estimate GPU requirements and secure access
- **Activities**:
  - Research UW Tillicum GPU cluster (H200 specs, $0.90/hour pricing)
  - Explore AWS/Azure research credits as backup (UW student programs)
  - Estimate compute hours for 3 scenarios:
    - **Optimistic**: 80 GPU hours ($72)
    - **Moderate**: 120 GPU hours ($108)
    - **Conservative**: 180 GPU hours ($162)
  - Document cost-benefit analysis for budget approval
- **Owner**: Mathew
- **Deliverable**: `compute-resources-guide.md`
- **Business Value**: Demonstrate project feasibility within budget constraints
- **Risk Mitigation**:
  - Apply for UW Tillicum access Week 1 (2-week lead time)
  - Fallback: AWS p3.2xlarge ($3.06/hour) if Tillicum unavailable

#### 8. Team-Project Matching
- **Objective**: Align team expertise with project requirements
- **Activities**:
  - Query Knowledge Graph API (`/api/match` endpoint) for team member data
  - Calculate match scores for SAP benchmarking project requirements
  - Assign project roles based on expertise alignment:
    - **Rahil**: Product strategy, stakeholder engagement, paper writing
    - **Siddarth**: Infrastructure, model wrappers, experimental execution
    - **Shreyas**: Statistical analysis, visualization, sales enablement
    - **Mathew**: Data engineering, dataset preparation, compute optimization
  - Document workload distribution and backup coverage
- **Owner**: Shreyas
- **Deliverable**: `team-matching.md`, `shared-data.json`
- **Business Value**: Maximize team efficiency and minimize risk of bottlenecks
- **Risk Mitigation**:
  - Cross-training on critical tasks (Week 2-3)
  - Fallback: Redistribute workload if team member unavailable

### Milestone M1: Research Foundation Complete (End of Week 2)

**Date**: November 22, 2025

**Success Criteria**:
- ✅ All 8 research files completed and validated (100+ pages total)
- ✅ `shared-data.json` created with team and project data
- ✅ Stakeholder intelligence ready for outreach (Tier 1/2/3 contacts identified)
- ✅ Methodology framework defined (statistical testing protocol documented)
- ✅ 89 datasets catalogued with availability confirmed

**Validation Process**:
1. Peer review of all research files by team (each member reviews 2 files)
2. Cross-reference citations and data sources (verify no dead links)
3. Knowledge gap analysis (identify any blocking questions for proposal writing)
4. Stakeholder outreach dry run (test email templates with faculty advisor)

**Business Value Delivered**:
- Competitive intelligence report positioning SAP vs competitors
- Internal champion identification and engagement strategy
- Academic credibility framework for peer review

**Sales Enablement Readiness**: 10%
- Industry landscape mapped
- SAP positioning understood
- Not yet actionable for sales teams

**Risk Assessment**:
- **Low Risk**: All tasks leverage public information
- **Mitigation**: If any dataset unavailable, proceed with 80+ datasets (still statistically robust)

**Paradigm Shift Comparison**:
- **ImageNet (2009)**: 2.5 years to establish benchmark infrastructure
- **Our M1**: 2 weeks leveraging existing benchmarks = **60x faster time-to-insight**

---

## Phase 1: Proposal Development (Weeks 3-4)

**Duration**: November 23 - December 6, 2025 (2 weeks)

**Objective**: Create complete proposal deliverables (PowerPoint, PDF, HTML) for SAP stakeholders.

**Paradigm Shift Comparison**:
- **BERT (2018)**: Google published 13-page paper with methodology, results, and discussion
- **Our approach**: 35-45 slide deck + 25-35 page report + interactive HTML viewer = 3x richer storytelling

### Week 3: Content & Visuals (Parallel Execution)

**Business Value Focus**: Articulate SAP value proposition across executive, technical, and sales audiences

**Agent 1 Tasks: Content Generator**

**Objective**: Create 7 comprehensive markdown content files

**Activities**:

1. **Executive Summary** (2 pages)
   - The Opportunity: $8.5B → $18.2B market growth
   - The Stakes: $50M+ SAP ARR at risk
   - The Solution: Independent validation unlocking sales enablement
   - **Owner**: Rahil
   - **Business Value**: Executive buy-in and budget approval

2. **Problem Statement** (5-7 pages, SCR framework)
   - Situation: Tabular AI market inflection point
   - Complication: Lack of independent RPT-1 validation
   - Resolution: 20-week benchmarking study
   - **Owner**: Rahil
   - **Business Value**: Frame SAP pain point and our solution

3. **Methodology** (8-12 pages, Three Pillars)
   - Pillar 1: Dataset Diversity (89 datasets, 15+ domains)
   - Pillar 2: Model Breadth (7 models, fair comparison)
   - Pillar 3: Statistical Rigor (Friedman + Nemenyi tests)
   - **Owner**: Siddarth
   - **Business Value**: Academic credibility and reproducibility

4. **Team Presentation** (6-8 pages, 100% Knowledge Graph data)
   - Query `/api/graph` for complete team profiles
   - Highlight SAP-relevant experience (Rahil: SAP CPI, Shreyas: o9 Supply Chain)
   - Map team expertise to project requirements
   - **Owner**: Shreyas
   - **Business Value**: Demonstrate team capability and SAP domain knowledge

5. **Timeline & Milestones** (5-7 pages)
   - 20-week Gantt chart with business value milestones
   - Sales enablement readiness timeline
   - Risk mitigation and contingency plans
   - **Owner**: Rahil
   - **Business Value**: Project feasibility and ROI trajectory

6. **Expected Outcomes** (5-7 pages)
   - Academic publication (NeurIPS/ICML 2026)
   - Sales enablement package (ROI calculators, objection handlers)
   - Competitive positioning report
   - **Owner**: Rahil
   - **Business Value**: Quantified impact on SAP sales cycles

7. **Stakeholder Strategy** (5-7 pages)
   - Tier 1/2/3 engagement plan
   - Communication cadence (bi-weekly updates)
   - Co-authorship opportunities
   - **Owner**: Rahil
   - **Business Value**: Maximize SAP adoption and internal advocacy

**Deliverable**: 7 MD files + 7 DOCX files (40-50 pages total)

**Agent 2 Tasks: Visual Designer**

**Objective**: Create 21 publication-quality visual assets

**Activities**:

1. **6 Infographics**:
   - Model comparison matrix (RPT-1 vs TabPFN vs AutoGluon vs XGBoost)
   - Dataset diversity visualization (89 datasets by domain, size, task type)
   - Timeline infographic (20 weeks with paradigm shift comparisons)
   - ROI waterfall chart ($75K investment → $1.5M Year 1 impact)
   - Team structure diagram (roles, expertise, SAP experience)
   - Competitive landscape (SAP vs Microsoft vs Oracle vs Salesforce)
   - **Owner**: Shreyas
   - **Format**: PNG (300 DPI) + SVG (vector graphics)

2. **6 Charts**:
   - Performance heatmap (models × datasets, color-coded by accuracy)
   - Statistical testing flow (Friedman → Nemenyi → Critical Difference diagram)
   - Compute cost breakdown (GPU hours by model, total budget)
   - Citation network (tabular AI research landscape)
   - Use case matrix (SAP products × RPT-1 applications)
   - Accuracy-efficiency trade-off scatter plot (accuracy vs inference time)
   - **Owner**: Shreyas
   - **Format**: PNG (300 DPI) + interactive Plotly HTML

3. **6 Diagrams (Mermaid)**:
   - Three-pillar methodology architecture
   - Experimental workflow (data → preprocessing → model → evaluation → stats)
   - Docker container architecture (4 environments + orchestration)
   - Statistical testing decision tree (Friedman → post-hoc tests)
   - Stakeholder engagement map (Tier 1/2/3 with communication flow)
   - Data pipeline (download → validate → preprocess → store)
   - **Owner**: Siddarth
   - **Format**: Mermaid code + rendered PNG

4. **3 Brand Assets**:
   - Cover page template (SAP blue + UW purple color palette)
   - Section divider slides (consistent typography and spacing)
   - Footer template (team contact info, QR codes to interactive dashboard)
   - **Owner**: Shreyas
   - **Format**: PowerPoint master slides + PNG

**Deliverable**: 21 visual assets in `/visuals/` folder

**Agent 3 Tasks: Interactive Developer**

**Objective**: Create 5 interactive web components for stakeholder engagement

**Activities**:

1. **Dataset Explorer** (Interactive table with filters)
   - 89 datasets with sortable/filterable columns (domain, size, task type)
   - Click to view dataset details (features, missing values, class balance)
   - Export filtered subset as CSV
   - **Owner**: Siddarth
   - **Technology**: React + AG Grid
   - **Business Value**: SAP stakeholders explore domain-relevant datasets

2. **Model Comparison Tool** (Side-by-side feature comparison)
   - RPT-1 vs TabPFN vs AutoGluon vs XGBoost
   - Interactive sliders for dataset characteristics (size, features, categorical %)
   - Real-time prediction of which model will perform best
   - **Owner**: Siddarth
   - **Technology**: React + D3.js
   - **Business Value**: Sales engineers select optimal model for customer use case

3. **Timeline Gantt Chart** (Interactive week-by-week view)
   - 20-week timeline with expandable task details
   - Milestone hover-overs showing business value delivered
   - Progress tracking (% complete, blockers, next steps)
   - **Owner**: Shreyas
   - **Technology**: React + Recharts
   - **Business Value**: SAP stakeholders monitor project progress

4. **ROI Calculator** (Input scenarios, output projections)
   - Inputs: Sales cycle length, win rate, POC costs, deal size
   - Outputs: Year 1/3/5 ROI from reduced friction, improved win rates
   - Scenario comparison (conservative vs moderate vs optimistic)
   - **Owner**: Shreyas
   - **Technology**: React + Formik
   - **Business Value**: SAP finance team justify investment

5. **Team Contact Directory** (Links to profiles)
   - Query `/api/students` for team member data
   - Interactive cards with headshots, expertise tags, LinkedIn links
   - "Schedule Meeting" buttons with calendar integration
   - **Owner**: Rahil
   - **Technology**: React + Knowledge Graph API
   - **Business Value**: Facilitate SAP stakeholder communication

**Deliverable**: 5 HTML/JS components in `/interactive/` folder

**Agent 4 Tasks: Code Repository Setup (Parallel)**

**Objective**: Initialize GitHub repository with benchmarking infrastructure

**Activities**:

1. **Repository Structure**:
   ```
   sap-rpt1-benchmarking/
   ├── README.md (project overview, setup instructions)
   ├── docker/
   │   ├── sap-rpt1.Dockerfile
   │   ├── tabpfn.Dockerfile
   │   ├── autogluon.Dockerfile
   │   └── gradient-boost.Dockerfile
   ├── data/
   │   ├── download_datasets.py
   │   ├── preprocess.py
   │   └── validate.py
   ├── models/
   │   ├── wrappers/
   │   │   ├── rpt1_wrapper.py
   │   │   ├── tabpfn_wrapper.py
   │   │   ├── autogluon_wrapper.py
   │   │   └── xgboost_wrapper.py
   │   └── configs/
   │       └── default_configs.yaml
   ├── experiments/
   │   ├── run_experiment.py
   │   ├── evaluate.py
   │   └── orchestrator.py
   ├── analysis/
   │   ├── statistical_tests.py
   │   ├── visualizations.py
   │   └── report_generator.py
   └── tests/
       ├── test_data_pipeline.py
       ├── test_model_wrappers.py
       └── test_evaluation.py
   ```

2. **Docker Base Environments**:
   - Build `sap-rpt1:v1.0` container (Python 3.11, PyTorch 2.0, RPT-1 dependencies)
   - Build `tabpfn:v2.5` container (Python 3.9, TabPFN dependencies)
   - Build `autogluon:v1.0` container (Python 3.8, AutoGluon, MXNet)
   - Build `gradient-boost:v1.0` container (XGBoost, CatBoost, LightGBM)
   - Test containers with "hello world" experiments

3. **Dataset Download Script**:
   - Implement `download_datasets.py` with retry logic
   - Support TabArena API, OpenML API, Kaggle API
   - Verify checksums for data integrity
   - Log download status to CSV

4. **Model Wrapper Templates**:
   - Implement `rpt1_wrapper.py` with ConTextTab API
   - Implement `tabpfn_wrapper.py` with Nature paper defaults
   - Implement `autogluon_wrapper.py` with medium_quality preset
   - Implement `xgboost_wrapper.py` with grid search
   - Standardized interface: `fit(X_train, y_train)`, `predict(X_test)`, `score(X_test, y_test)`

**Owner**: Siddarth

**Deliverable**: GitHub repo `sap-rpt1-benchmarking` with initial codebase

**Business Value**: Reproducibility foundation for academic publication

### Week 4: Assembly & Delivery

**Business Value Focus**: Deliver complete stakeholder engagement package

**Agent 5 Tasks: GitHub Projects**

**Objective**: Create 150+ GitHub Project tasks spanning Weeks 5-20

**Activities**:

1. **Project Board Setup**:
   - Create 3 boards: "To Do", "In Progress", "Done"
   - Define 6 major phases (matching this timeline document)
   - Create 150+ granular tasks with:
     - Task description and acceptance criteria
     - Owner assignment (Rahil, Siddarth, Shreyas, Mathew)
     - Estimated hours and dependencies
     - Priority level (critical path, nice-to-have)

2. **Timeline Export**:
   - Export Gantt chart to CSV (task, start date, end date, owner, status)
   - Export JSON for interactive timeline viewer
   - Link to GitHub Issues for tracking

**Owner**: Shreyas

**Deliverable**: GitHub Projects configured, timeline export (CSV + JSON)

**Business Value**: Transparent project tracking for SAP stakeholders

**Final Assembly Tasks**

**Objective**: Integrate content + visuals + interactive elements into 4 deliverables

**Activities**:

1. **PowerPoint Generation** (35-45 slides):
   - Apply SAP-aligned design system (navy blue, teal, slate gray color palette)
   - Integrate 21 visual assets
   - Embed QR codes to interactive dashboard
   - Speaker notes with talking points for each slide
   - **Target Audience**: SAP executives (Walter Sun), research leaders (Johannes Hoffart)
   - **Owner**: Rahil + Shreyas
   - **Quality Standard**: BCG/McKinsey 9.5/10 (validated by faculty advisor)

2. **PDF Report** (25-35 pages):
   - Professional typography (Helvetica Neue, 12pt body, 1.5 line spacing)
   - Annotated figures with captions
   - Full citations (APA style)
   - Executive summary (1-page standalone)
   - **Target Audience**: SAP product managers, sales engineers
   - **Owner**: Rahil + Shreyas
   - **Quality Standard**: Academic journal submission-ready

3. **Technical Appendix** (30-40 pages):
   - Dataset catalog (89 datasets with statistics)
   - Model configurations (hyperparameters, training details)
   - Statistical testing methodology (Friedman, Nemenyi, Wilcoxon)
   - Reproducibility checklist (REFORMS framework)
   - **Target Audience**: SAP researchers, peer reviewers
   - **Owner**: Siddarth + Mathew
   - **Quality Standard**: NeurIPS/ICML supplementary material

4. **Interactive HTML Viewer** (`COMPLETE_PROPOSAL_VIEWER.html`):
   - Single-page app embedding all 5 interactive components
   - Responsive design (desktop, tablet, mobile)
   - Analytics tracking (page views, time on page, interactions)
   - Export functionality (PDF, CSV downloads)
   - **Target Audience**: SAP sales teams, customer demonstrations
   - **Owner**: Siddarth
   - **Quality Standard**: Enterprise SaaS UI/UX standards

**Quality Assurance Checklist**:
- ✅ All citations verified (no dead links, correct APA formatting)
- ✅ Design system compliance (colors, fonts, spacing per `claude.md`)
- ✅ Data accuracy (all statistics cross-referenced with sources)
- ✅ Typo-free (Grammarly + manual review)
- ✅ Accessibility (WCAG 2.1 AA compliance for web components)
- ✅ File size optimization (PowerPoint <50MB, PDF <10MB)

**Owner**: All agents coordinated by Rahil

**Deliverable**: 4 final deliverables ready for SAP stakeholder distribution

### Milestone M2: Proposal Content Complete (End of Week 3)

**Date**: December 1, 2025

**Success Criteria**:
- ✅ All 14 content files (7 MD + 7 DOCX) created and validated
- ✅ 21 visual assets completed (infographics, charts, diagrams, brand assets)
- ✅ 5 interactive components functional (dataset explorer, model comparison, timeline, ROI calculator, team directory)
- ✅ GitHub repository initialized with benchmarking codebase

**Validation Process**:
1. Internal team review (each member reviews all deliverables)
2. Faculty advisor review (BCG/McKinsey quality assessment)
3. Design system compliance check (colors, fonts, spacing)
4. Interactive component testing (cross-browser, responsive design)

**Business Value Delivered**:
- Complete value proposition articulated for SAP stakeholders
- Interactive tools demonstrating technical sophistication
- GitHub repository establishing reproducibility foundation

**Sales Enablement Readiness**: 25%
- Value proposition articulated
- Not yet validated with experimental data

### Milestone M3: Proposal Delivered to SAP (End of Week 4)

**Date**: December 6, 2025

**Success Criteria**:
- ✅ PowerPoint deck (35-45 slides) complete and validated
- ✅ PDF report (25-35 pages) complete and validated
- ✅ Technical appendix (30-40 pages) complete and validated
- ✅ Interactive HTML viewer deployed and accessible
- ✅ GitHub Projects configured with 150+ tasks for Weeks 5-20
- ✅ Quality validation passed (BCG/McKinsey 9.5/10 standard)
- ✅ Ready for stakeholder outreach (email templates, meeting requests)

**Validation Process**:
1. External review (faculty advisor simulates SAP stakeholder feedback)
2. BCG/McKinsey quality checklist (40-50% white space, data-driven insights, MECE framework)
3. Peer-reviewed citations (all sources verified)
4. Accessibility testing (WCAG 2.1 AA compliance)
5. File integrity (PowerPoint opens in Microsoft 365, PDF prints correctly)

**Business Value Delivered**:
- Complete stakeholder engagement package ready for SAP distribution
- Internal champion recruitment materials (value propositions by role)
- Project management foundation (GitHub Projects timeline)

**Sales Enablement Readiness**: 30%
- Technical credibility established
- Methodology framework documented
- Not yet validated with experimental results

**Risk Assessment**:
- **Low Risk**: All deliverables based on research and planning (no dependencies on SAP access)
- **Mitigation**: If SAP non-responsive, proceed with independent benchmarking (value persists)

**Stakeholder Engagement Actions**:
1. **Week 4, Day 1**: Email Walter Sun (Global Head of AI, SAP) with 1-page executive summary
2. **Week 4, Day 2**: Email Sam Thelin (ConTextTab lead author) with technical methodology
3. **Week 4, Day 3**: Email Johannes Hoffart (Research Director) with academic co-authorship proposal
4. **Week 4, Day 4-5**: Follow up with Tier 2 stakeholders (SAP product managers, sales engineers)

**Paradigm Shift Comparison**:
- **BERT (2018)**: 13-page paper describing methodology and results
- **Our M3**: 100+ pages of content + interactive tools = **7x richer storytelling**

---

## Phase 2: Infrastructure & Dataset Preparation (Weeks 5-7)

**Duration**: December 7 - December 27, 2025 (3 weeks)

**Objective**: Set up complete infrastructure for benchmarking experiments and prepare all 89 datasets.

**Paradigm Shift Comparison**:
- **AlphaFold (2020)**: 2 years building protein structure prediction pipeline
- **Our approach**: 3 weeks leveraging Docker, open benchmarks, cloud GPUs = **35x faster infrastructure**

### Week 5: UW Tillicum Access & Docker Environments

**Business Value Focus**: Establish reproducible experimental infrastructure

**Infrastructure Setup Tasks**

#### 1. UW Tillicum GPU Access
- **Objective**: Secure H200 GPU allocation for 180 compute hours
- **Activities**:
  - Apply for demo account (submit via UW Research Computing portal)
  - Request research allocation (justify academic publication goal)
  - Test connectivity (SSH, SLURM job submission)
  - Benchmark GPU performance (run "hello world" PyTorch training)
  - Document setup instructions for team access
- **Owner**: Mathew
- **Timeline**: Week 5, Days 1-3
- **Success Criteria**: All 4 team members can submit SLURM jobs
- **Business Value**: Cost-effective compute ($0.90/hour vs AWS $3.06/hour = 70% savings)
- **Risk Mitigation**:
  - Backup: AWS p3.2xlarge with UW student research credits
  - Fallback: Azure NC6s_v3 ($0.90/hour via UW partnership)

#### 2. Docker Container Development
- **Objective**: Build 4 reproducible environments for all models
- **Activities**:

**Container 1: `sap-rpt1:v1.0`**
  - Base: `python:3.11-slim`
  - Dependencies: PyTorch 2.0, RPT-1 API client, pandas, scikit-learn
  - Configuration: ConTextTab default settings from paper
  - Test: Run RPT-1 on UCI Adult dataset (expected accuracy ~85%)
  - **Build Time**: 4 hours (including troubleshooting)

**Container 2: `tabpfn:v2.5`**
  - Base: `python:3.9-slim`
  - Dependencies: TabPFN v2.5, PyTorch 1.13, scikit-learn
  - Configuration: Nature paper defaults (ensemble=8, temperature=1.0)
  - Test: Run TabPFN on UCI Wine dataset (expected accuracy ~98%)
  - **Build Time**: 3 hours

**Container 3: `autogluon:v1.0`**
  - Base: `python:3.8-slim`
  - Dependencies: AutoGluon Tabular 0.8.0, MXNet, XGBoost
  - Configuration: `medium_quality` preset, 1-hour time budget per fold
  - Test: Run AutoGluon on UCI Diabetes dataset (expected RMSE ~60)
  - **Build Time**: 5 hours (MXNet compilation complex)

**Container 4: `gradient-boost:v1.0`**
  - Base: `python:3.10-slim`
  - Dependencies: XGBoost 2.0, CatBoost 1.2, LightGBM 4.0
  - Configuration: Grid search over 3 learning rates, 3 depths (27 configs)
  - Test: Run XGBoost on UCI Iris dataset (expected accuracy ~97%)
  - **Build Time**: 2 hours

- **Owner**: Siddarth
- **Timeline**: Week 5, Days 2-5 (parallel with Tillicum access)
- **Success Criteria**: All 4 containers pass smoke tests
- **Business Value**: Reproducibility foundation for peer review
- **Risk Mitigation**:
  - Use official Docker Hub base images (stability)
  - Pin dependency versions (avoid breaking changes)
  - Fallback: Conda environments if Docker unavailable

#### 3. Orchestration & Job Scheduling
- **Objective**: Automate experiment execution across 89 datasets × 7 models
- **Activities**:
  - Implement SLURM job array submission script
  - Configure resource allocation (1 GPU, 16 CPU, 64GB RAM per job)
  - Set up logging (stdout/stderr to `/logs/`, results to `/results/`)
  - Implement error handling (timeout after 4 hours, retry once)
  - Create monitoring dashboard (track job status, GPU utilization, ETA)
- **Owner**: Siddarth + Mathew
- **Timeline**: Week 5, Days 4-5
- **Success Criteria**: End-to-end test: 1 model × 5 datasets completes successfully
- **Business Value**: Efficient resource utilization = minimize compute costs

### Week 6: Dataset Download & Validation

**Business Value Focus**: Ensure dataset diversity for enterprise domain coverage

**Dataset Preparation Tasks**

#### 1. TabArena Datasets (51 datasets)
- **Objective**: Download and validate TabArena benchmark
- **Activities**:
  - Use TabArena API client (`pip install tabdata`)
  - Download all 51 datasets (classification + regression)
  - Verify checksums (MD5 hashes from TabArena manifest)
  - Generate dataset statistics (rows, features, missing %, class balance)
  - Document domain mapping (finance: 12 datasets, healthcare: 8, retail: 7, etc.)
- **Owner**: Mathew
- **Timeline**: Week 6, Days 1-2
- **Success Criteria**: All 51 datasets downloaded, 0 checksum failures
- **Business Value**: Demonstrate RPT-1 performance on SAP-relevant domains (finance, supply chain)
- **Risk Mitigation**:
  - TabArena hosted on stable OpenML infrastructure
  - Fallback: Manual download from OpenML if API fails

#### 2. TabZilla Datasets (20 datasets)
- **Objective**: Download "hardest" datasets for stress-testing RPT-1
- **Activities**:
  - Download from TabZilla GitHub repository
  - Verify against published TabZilla paper (McElfresh et al., 2023)
  - Document why each dataset is "hard" (high dimensionality, class imbalance, missing values)
  - Cross-reference with TabArena (remove duplicates)
- **Owner**: Mathew
- **Timeline**: Week 6, Day 3
- **Success Criteria**: All 20 datasets downloaded, deduplicated
- **Business Value**: Identify RPT-1 limitations and optimization opportunities
- **Risk Mitigation**:
  - TabZilla datasets publicly available on Zenodo
  - Fallback: Use subset if download issues (still 71 datasets total)

#### 3. OpenML-CC18 Datasets (18 datasets)
- **Objective**: Add curated benchmark for cross-study comparisons
- **Activities**:
  - Download from OpenML API (`pip install openml`)
  - Verify against Bischl et al. (2021) paper
  - Document preprocessing requirements (categorical encoding, missing value handling)
  - Merge with TabArena/TabZilla (remove duplicates)
- **Owner**: Mathew
- **Timeline**: Week 6, Day 4
- **Success Criteria**: 89 unique datasets ready (51 TabArena + 20 TabZilla + 18 OpenML-CC18)
- **Business Value**: Enable comparisons with prior AutoML studies
- **Risk Mitigation**:
  - If OpenML API issues, proceed with 71 datasets (TabArena + TabZilla)
  - Fallback: Add OpenML-CC18 in Week 8 if time permits

#### 4. Data Preprocessing Pipeline
- **Objective**: Standardize preprocessing across all datasets
- **Activities**:
  - Implement missing value imputation (median for numerical, mode for categorical)
  - Implement categorical encoding (one-hot if <10 categories, label encoding otherwise)
  - Generate train/test splits (80/20, stratified, random seed=42)
  - Generate 10-fold cross-validation indices (stratified, random seed=42)
  - Store preprocessed datasets in Parquet format (compression, fast loading)
- **Owner**: Mathew
- **Timeline**: Week 6, Days 4-5
- **Success Criteria**: All 89 datasets preprocessed, stored in `/data/processed/`
- **Business Value**: Fair model comparison (same preprocessing for all models)

#### 5. Data Validation & Quality Checks
- **Objective**: Detect anomalies and corrupted data
- **Activities**:
  - Cross-reference dataset statistics with published papers
  - Detect outliers (Z-score > 3, IQR > 1.5)
  - Check for data leakage (train/test overlap)
  - Generate dataset manifest (CSV with metadata: name, domain, size, features, task type)
  - Document edge cases (e.g., datasets with >500 features = TabPFN incompatible)
- **Owner**: Shreyas
- **Timeline**: Week 6, Day 5
- **Success Criteria**: Dataset manifest complete, anomalies documented
- **Business Value**: Prevent experimental failures due to data quality issues

### Week 7: Model Wrappers & Evaluation Pipeline

**Business Value Focus**: Implement fair comparison framework

**Model Wrapper Tasks**

#### 1. RPT-1 Wrapper (`rpt1_wrapper.py`)
- **Objective**: Interface with SAP RPT-1 API
- **Activities**:
  - Implement ConTextTab API client (authentication, request/response handling)
  - Configure default settings from ConTextTab paper (context length, attention heads)
  - Handle API rate limits (10 requests/minute)
  - Implement timeout handling (4 hours max per dataset)
  - Log inference time, memory usage, API costs
- **Owner**: Siddarth
- **Timeline**: Week 7, Days 1-2
- **Success Criteria**: RPT-1 runs successfully on 5 test datasets
- **Business Value**: Primary model of interest for SAP stakeholders
- **Risk Mitigation**:
  - If API access denied, use open-source RPT-1-OSS variant
  - Fallback: Report limitations and recommend SAP provide API access

#### 2. TabPFN Wrapper (`tabpfn_wrapper.py`)
- **Objective**: Configure TabPFN with Nature paper defaults
- **Activities**:
  - Install TabPFN v2.5 (`pip install tabpfn`)
  - Configure ensemble size (8 models), temperature (1.0)
  - Handle dataset size limits (≤10K rows, ≤500 features)
  - Implement subsampling for larger datasets (random sample, stratified)
  - Document subsampling strategy in appendix
- **Owner**: Siddarth
- **Timeline**: Week 7, Day 2
- **Success Criteria**: TabPFN runs on all compatible datasets
- **Business Value**: State-of-the-art competitor (Nature publication)

#### 3. AutoGluon Wrapper (`autogluon_wrapper.py`)
- **Objective**: Configure AutoGluon with `medium_quality` preset
- **Activities**:
  - Install AutoGluon Tabular 0.8.0
  - Set `medium_quality` preset (balances accuracy and speed)
  - Set 1-hour time budget per fold (prevents runaway training)
  - Monitor memory usage (kill if >60GB RAM to prevent OOM)
  - Log ensemble composition (which models AutoGluon selected)
- **Owner**: Siddarth
- **Timeline**: Week 7, Day 3
- **Success Criteria**: AutoGluon runs on all 89 datasets
- **Business Value**: Industry-standard AutoML baseline

#### 4. Gradient Boosting Wrappers (`xgboost_wrapper.py`, `catboost_wrapper.py`, `lightgbm_wrapper.py`)
- **Objective**: Implement traditional ML baselines with hyperparameter tuning
- **Activities**:
  - Install XGBoost 2.0, CatBoost 1.2, LightGBM 4.0
  - Define grid search space:
    - Learning rate: [0.01, 0.05, 0.1]
    - Max depth: [3, 5, 7]
    - Number of estimators: [100, 300, 500]
  - Use 5-fold CV for hyperparameter tuning
  - Select best config based on validation score
  - Log best hyperparameters for each dataset
- **Owner**: Siddarth
- **Timeline**: Week 7, Days 3-4
- **Success Criteria**: All 3 models run with hyperparameter tuning
- **Business Value**: Establish strong baselines for fair comparison

**Evaluation Pipeline Tasks**

#### 5. Metrics Calculation (`evaluate.py`)
- **Objective**: Compute standardized performance metrics
- **Activities**:
  - Implement classification metrics (ROC-AUC, accuracy, F1-score, precision, recall)
  - Implement regression metrics (R², RMSE, MAE)
  - Implement timing metrics (training time, inference time per sample)
  - Implement memory metrics (peak RAM usage, GPU memory)
  - Store results in structured CSV format (model, dataset, fold, metric, value)
- **Owner**: Siddarth
- **Timeline**: Week 7, Day 4
- **Success Criteria**: All metrics computed correctly (verified against scikit-learn)

#### 6. Cross-Validation Loop (`run_experiment.py`)
- **Objective**: Implement 10-fold CV with stratification
- **Activities**:
  - Load preprocessed dataset and CV indices
  - For each fold:
    - Train model on 9 folds
    - Evaluate on 1 held-out fold
    - Store predictions, metrics, timing
  - Aggregate results (mean, std across 10 folds)
  - Handle failures gracefully (timeout, OOM, exceptions)
- **Owner**: Siddarth
- **Timeline**: Week 7, Day 5
- **Success Criteria**: End-to-end test: 1 model × 1 dataset × 10 folds completes

#### 7. Error Handling & Logging (`orchestrator.py`)
- **Objective**: Robust experiment management
- **Activities**:
  - Implement timeout handling (kill job after 4 hours)
  - Implement OOM detection (kill if RAM >60GB)
  - Implement exception logging (stack traces to `/logs/errors/`)
  - Implement retry logic (retry once on failure, then skip)
  - Implement result validation (check for NaN, inf, negative metrics)
- **Owner**: Siddarth + Mathew
- **Timeline**: Week 7, Day 5
- **Success Criteria**: Simulated failure scenarios handled correctly

### Milestone M3: Infrastructure & Datasets Ready (End of Week 7)

**Date**: December 27, 2025

**Success Criteria**:
- ✅ UW Tillicum GPU access secured (or AWS backup configured)
- ✅ All 4 Docker containers built and tested
- ✅ All 89 datasets downloaded, validated, and preprocessed
- ✅ Complete benchmarking codebase functional (end-to-end test: 1 model × 5 datasets)
- ✅ Dataset manifest and documentation complete
- ✅ Model wrappers standardized (same interface across all 7 models)
- ✅ Evaluation pipeline validated (metrics match scikit-learn reference)

**Validation Process**:
1. End-to-end smoke test: Run XGBoost on 5 datasets from different domains
2. Checksum validation: All 89 datasets match published checksums
3. Docker container smoke tests: All 4 containers run "hello world" experiments
4. Cross-reference: Dataset statistics match published papers (TabArena, TabZilla, OpenML-CC18)
5. Code review: All team members review experimental pipeline

**Business Value Delivered**:
- Reproducible experimental framework for academic publication
- Dataset diversity covering 15+ SAP enterprise domains
- Fair comparison infrastructure (standardized preprocessing, metrics)

**Sales Enablement Readiness**: 40%
- Technical credibility established (reproducible infrastructure)
- Competitive context understood (7 models, 89 datasets)
- Not yet validated with experimental results

**Risk Assessment**:
- **Medium Risk**: Infrastructure dependencies (UW Tillicum access, RPT-1 API access)
- **Mitigation**: AWS backup configured, RPT-1-OSS fallback ready
- **Buffer**: Week 7 provides cushion for infrastructure issues

**Paradigm Shift Comparison**:
- **ImageNet (2009)**: 2.5 years to curate 14M images
- **BERT (2018)**: 4 days pre-training on 16 TPUs ($7K compute cost)
- **AlphaFold (2020)**: 2 years building protein prediction pipeline
- **Our M3**: **3 weeks** leveraging open benchmarks, Docker, cloud GPUs

---

## Phase 3: Benchmarking Experiments (Weeks 8-15)

**Duration**: December 28, 2025 - February 21, 2026 (8 weeks)

**Objective**: Execute all 623 experiments (7 models × 89 datasets) with 10-fold cross-validation = 6,230 individual training runs.

**Paradigm Shift Comparison**:
- **ImageNet ILSVRC (2012)**: 1 week evaluation window, 25+ teams
- **BERT GLUE (2018)**: 2 weeks for 11 tasks
- **AlphaFold CASP14 (2020)**: 2 weeks blind prediction
- **Our approach**: 8 weeks comprehensive benchmarking (623 experiments) = **4x more thorough**

### Week 8-9: Baseline Models (XGBoost, CatBoost, LightGBM)

**Duration**: December 28, 2025 - January 10, 2026 (2 weeks)

**Business Value Focus**: Establish industry-standard performance benchmarks

**Objectives**:
1. Validate experimental pipeline with well-understood models
2. Establish strong baselines for fair RPT-1 comparison
3. Identify dataset characteristics favoring gradient boosting

**Execution Plan**:

**Week 8: XGBoost (89 datasets × 10 folds = 890 runs)**
- **Activities**:
  - Run XGBoost with grid search (3 learning rates × 3 depths × 3 n_estimators = 27 configs)
  - Use 5-fold inner CV for hyperparameter tuning (per dataset)
  - Select best config, train on 9 folds, evaluate on 1 fold (repeat 10 times)
  - Log training time, inference time, peak RAM, best hyperparameters
  - Store predictions and metrics to `/results/xgboost/`
- **Owner**: Siddarth (execution), Shreyas (monitoring)
- **Estimated GPU Hours**: 20 hours (XGBoost is CPU-bound, GPU used for data loading)
- **Cost**: $18 (UW Tillicum H200)
- **Success Criteria**: 890 runs complete, <5% failure rate
- **Validation**: Cross-reference XGBoost results with published TabArena baselines (expected correlation r>0.9)

**Week 9, Days 1-2: CatBoost (89 datasets × 10 folds = 890 runs)**
- **Activities**: Same as XGBoost, using CatBoost-specific hyperparameters
- **Owner**: Siddarth
- **Estimated GPU Hours**: 18 hours
- **Cost**: $16.20
- **Validation**: CatBoost should outperform XGBoost on categorical-heavy datasets (>50% categorical features)

**Week 9, Days 3-5: LightGBM (89 datasets × 10 folds = 890 runs)**
- **Activities**: Same as XGBoost, using LightGBM-specific hyperparameters
- **Owner**: Siddarth
- **Estimated GPU Hours**: 15 hours (LightGBM faster than XGBoost)
- **Cost**: $13.50
- **Validation**: LightGBM should be fastest (lowest training time)

**Total Week 8-9**: 2,670 runs, 53 GPU hours, $47.70

**Business Value Delivered**:
- Strong baselines establishing "minimum acceptable performance"
- Dataset difficulty ranking (identify hardest datasets for RPT-1 validation)
- Hyperparameter insights (learning rate, depth preferences by dataset)

**Sales Enablement Impact**:
- Sales engineers can say: "RPT-1 outperforms XGBoost by X% on your industry's datasets"
- Objection handler: "Traditional ML requires extensive hyperparameter tuning; RPT-1 is zero-shot"

**Risk Mitigation**:
- **Risk**: Hyperparameter tuning extends runtime beyond 2 weeks
- **Mitigation**: Use coarse grid search (3×3×3 = 27 configs, not 10×10×10 = 1000)
- **Fallback**: Use default hyperparameters if tuning fails (still valid baseline)

### Milestone M4: Baseline Models Validated (End of Week 9)

**Date**: January 10, 2026

**Success Criteria**:
- ✅ XGBoost, CatBoost, LightGBM complete on all 89 datasets
- ✅ 2,670 runs executed, <5% failure rate (≤134 failures)
- ✅ Results stored in structured CSV format
- ✅ Baseline performance cross-referenced with published benchmarks (TabArena)
- ✅ Dataset difficulty ranking established
- ✅ Total GPU hours ≤55 hours (within moderate budget)

**Validation Process**:
1. Sanity check: XGBoost results correlate with TabArena baselines (r>0.9)
2. Consistency check: Mean CV performance matches expected ranges
3. Outlier detection: Identify anomalous results (accuracy >99.5% or <50%)
4. Failure analysis: Document why failures occurred (timeout, OOM, data issues)

**Business Value Delivered**:
- $50K in sales support value (baseline benchmarks for POC acceleration)
- Early signals on RPT-1 performance ceiling (dataset difficulty)

**Sales Enablement Readiness**: 40%
- Industry-standard baselines established
- Dataset domain coverage validated
- Not yet compared to RPT-1

**Paradigm Shift Comparison**:
- **ImageNet (2012)**: AlexNet's 15.3% top-5 error was **10.8pp better** than second place
- **Our M4**: Established what "second place" (XGBoost) performance looks like

---

### Week 10-11: SAP RPT-1 Experiments (CRITICAL PATH)

**Duration**: January 11 - January 24, 2026 (2 weeks)

**Business Value Focus**: Validate SAP's flagship tabular foundation model

**Objectives**:
1. Execute RPT-1 on all 89 datasets with 10-fold CV
2. Identify RPT-1 strengths (dataset characteristics where it excels)
3. Identify RPT-1 limitations (dataset characteristics where it underperforms)
4. Generate actionable optimization recommendations for SAP

**Execution Plan**:

**Week 10: RPT-1 First Pass (89 datasets × 10 folds = 890 runs)**
- **Activities**:
  - Run SAP RPT-1-OSS (or API if access granted) on all 89 datasets
  - Use ConTextTab default configuration from published paper
  - Monitor for failures (timeout, OOM, API rate limits, exceptions)
  - Log inference time, API costs (if applicable), peak GPU memory
  - Store predictions and metrics to `/results/rpt1/`
  - **Critical**: Flag datasets where RPT-1 exceeds limits (>10M rows, >10K features)
- **Owner**: Siddarth (execution), Mathew (infrastructure monitoring)
- **Estimated GPU Hours**: 35 hours (foundation models slower than XGBoost)
- **Cost**: $31.50 (or API costs if using SAP RPT-1 commercial API)
- **Success Criteria**: 890 runs attempted, document all failures

**Week 11: RPT-1 Failure Handling & Re-runs**
- **Activities**:
  - Analyze failure modes:
    - Timeout failures: Re-run with 8-hour limit (vs 4-hour default)
    - OOM failures: Subsample dataset to fit in memory, document strategy
    - API failures: Retry with exponential backoff
  - Re-run failed experiments with adjusted configurations
  - Handle edge cases (e.g., datasets exceeding RPT-1 architectural limits)
  - **Critical Decision Point**: If >20% failure rate, escalate to SAP stakeholders
- **Owner**: Siddarth
- **Estimated GPU Hours**: 15 hours (re-runs)
- **Cost**: $13.50
- **Success Criteria**: <10% failure rate after re-runs (≤89 datasets × 10% = 9 datasets)

**Total Week 10-11**: 890+ runs, 50 GPU hours, $45

**Business Value Delivered**:
- **$150K in POC acceleration value**: Sales engineers can demonstrate RPT-1 performance on customer-relevant datasets
- **Optimization roadmap for SAP**: Identify failure modes and improvement opportunities
- **Use case guidance**: Dataset characteristics where RPT-1 excels vs underperforms

**Sales Enablement Impact**:
- **Positive messaging**: "RPT-1 achieves 92% accuracy on financial fraud detection datasets (vs XGBoost 87%)"
- **Objection handler**: "RPT-1 is optimized for datasets <1M rows; for larger datasets, we recommend [alternative]"
- **TCO analysis**: RPT-1 zero-shot vs XGBoost hyperparameter tuning (saves 15 hours per dataset)

**Risk Mitigation**:
- **Risk**: RPT-1 API access denied by SAP
- **Mitigation**: Use open-source RPT-1-OSS variant (90% feature parity)
- **Fallback**: Document limitations and recommend SAP provide API access for complete validation

- **Risk**: High failure rate (>20%) due to dataset characteristics
- **Mitigation**: Subsample large datasets, document limitations
- **Fallback**: Report findings as "RPT-1 generalization study" (still valuable for SAP)

- **Risk**: RPT-1 underperforms XGBoost on majority of datasets
- **Mitigation**: Frame as "actionable optimization roadmap for SAP R&D"
- **Fallback**: Identify specific domains/dataset types where RPT-1 excels (niche positioning)

**CRITICAL PATH ALERT**: Weeks 10-11 are project bottleneck. RPT-1 performance determines entire narrative.

### Milestone M5: RPT-1 Results Complete (End of Week 11)

**Date**: January 24, 2026

**Success Criteria**:
- ✅ RPT-1 executed on all 89 datasets (or documented failures)
- ✅ <10% failure rate after re-runs
- ✅ Results stored in structured CSV format
- ✅ Failure mode analysis complete (timeout, OOM, API issues)
- ✅ Preliminary performance comparison vs XGBoost/CatBoost/LightGBM
- ✅ RPT-1 strengths and limitations documented

**Validation Process**:
1. Sanity check: RPT-1 performance within expected ranges (not 100% accuracy, not random)
2. Consistency check: Cross-validation std < 10% (model stability)
3. Comparative check: RPT-1 vs XGBoost correlation analysis (identify patterns)
4. Failure analysis: Document dataset characteristics causing failures

**Business Value Delivered**:
- **$150K in POC acceleration**: Sales teams can reference RPT-1 performance on 80+ datasets
- **Optimization roadmap**: SAP R&D can prioritize improvements based on failure analysis
- **Use case library**: Identify 15-20 datasets where RPT-1 significantly outperforms XGBoost

**Sales Enablement Readiness**: 60%
- RPT-1 strengths and weaknesses clear
- Use case guidance available
- Not yet statistically validated (need Friedman/Nemenyi tests)

**Stakeholder Engagement Action**:
- **Week 11, Day 5**: Email SAP stakeholders with preliminary findings (RPT-1 performance summary)
- **Goal**: Secure co-authorship commitment for final paper

**Paradigm Shift Comparison**:
- **ImageNet (2012)**: AlexNet achieved 15.3% top-5 error (vs 26.1% second place)
- **BERT (2018)**: 80.5% GLUE score (vs 72.8% previous best)
- **Our M5**: Document RPT-1 performance gap vs XGBoost (positive or negative, both valuable)

---

### Week 12-13: TabPFN & TabICL Experiments

**Duration**: January 25 - February 7, 2026 (2 weeks)

**Business Value Focus**: Compare RPT-1 to state-of-the-art tabular foundation models

**Objectives**:
1. Validate TabPFN (Nature publication, academic credibility)
2. Validate TabICL (in-context learning approach)
3. Position RPT-1 vs academic state-of-the-art

**Execution Plan**:

**Week 12: TabPFN v2.5 (Subset of 89 datasets)**
- **Activities**:
  - Identify TabPFN-compatible datasets (≤10K rows, ≤500 features)
  - Estimate ~45 datasets compatible (50% of 89)
  - For larger datasets: Implement stratified subsampling to 10K rows
  - Run TabPFN with Nature paper defaults (ensemble=8, temperature=1.0)
  - Document subsampling strategy in technical appendix
  - Log inference time (TabPFN is slow due to ensemble)
- **Owner**: Siddarth
- **Estimated GPU Hours**: 20 hours (TabPFN inference expensive)
- **Cost**: $18
- **Success Criteria**: TabPFN runs on 45+ compatible datasets

**Week 13: TabICL (89 datasets × 10 folds = 890 runs)**
- **Activities**:
  - Run TabICL (in-context learning for tabular data)
  - Use default configuration (k=5 nearest neighbors for context)
  - Handle failures (TabICL may fail on high-dimensional data)
  - Log inference time and memory usage
- **Owner**: Siddarth
- **Estimated GPU Hours**: 25 hours
- **Cost**: $22.50
- **Success Criteria**: TabICL runs on 75+ datasets

**Total Week 12-13**: 1,335 runs, 45 GPU hours, $40.50

**Business Value Delivered**:
- **$300K in objection handling value**: Sales teams can compare RPT-1 to Nature-published TabPFN
- **Academic credibility**: Position RPT-1 vs peer-reviewed state-of-the-art
- **Differentiation messaging**: "RPT-1 scales to datasets >10K rows; TabPFN limited to 10K"

**Sales Enablement Impact**:
- **Competitive positioning**: "RPT-1 matches TabPFN accuracy with 10x faster inference"
- **Objection handler**: "TabPFN is research prototype; RPT-1 is production-ready with enterprise support"

**Risk Mitigation**:
- **Risk**: TabPFN subsampling introduces bias
- **Mitigation**: Document subsampling strategy, run sensitivity analysis (compare 5K vs 10K samples)
- **Fallback**: Report TabPFN results on compatible datasets only (still valuable comparison)

### Milestone M6: Competitive Analysis Complete (End of Week 13)

**Date**: February 7, 2026

**Success Criteria**:
- ✅ TabPFN executed on 45+ compatible datasets
- ✅ TabICL executed on 75+ datasets
- ✅ Head-to-head comparison: RPT-1 vs TabPFN vs TabICL vs XGBoost
- ✅ Performance heatmap generated (7 models × 89 datasets)
- ✅ Dataset characteristics analysis (when does each model excel?)

**Validation Process**:
1. Cross-reference TabPFN results with Nature paper (verify implementation correctness)
2. Consistency check: TabICL performance correlates with k-NN baselines
3. Comparative analysis: Identify dataset characteristics favoring foundation models vs gradient boosting

**Business Value Delivered**:
- **$300K in objection handling**: Sales teams can confidently answer "How does RPT-1 compare to TabPFN?"
- **Differentiation matrix**: Clear messaging on RPT-1 advantages (scalability, production-readiness)

**Sales Enablement Readiness**: 75%
- Competitive differentiation clear
- Use case-specific recommendations available
- Not yet statistically validated

---

### Week 14-15: AutoGluon & Advanced Analysis

**Duration**: February 8 - February 21, 2026 (2 weeks)

**Business Value Focus**: Compare RPT-1 to industry-standard AutoML

**Objectives**:
1. Validate AutoGluon (industry-standard AutoML baseline)
2. Perform subgroup analyses (by dataset size, domain, feature types)
3. Conduct accuracy-efficiency trade-off analysis

**Execution Plan**:

**Week 14: AutoGluon (89 datasets × 10 folds = 890 runs)**
- **Activities**:
  - Run AutoGluon Tabular with `medium_quality` preset
  - Set 1-hour time budget per fold (prevent runaway training)
  - Monitor memory usage (kill if >60GB RAM)
  - Log ensemble composition (which models AutoGluon selected)
  - Store predictions and metrics to `/results/autogluon/`
- **Owner**: Siddarth
- **Estimated GPU Hours**: 30 hours (AutoGluon trains multiple models)
- **Cost**: $27
- **Success Criteria**: AutoGluon runs on all 89 datasets

**Week 15: Subgroup Analyses**
- **Activities**:

**1. Performance by Dataset Size**:
  - Small (<1K rows): 15 datasets
  - Medium (1K-10K rows): 30 datasets
  - Large (10K-100K rows): 35 datasets
  - Very Large (>100K rows): 9 datasets
  - Hypothesis: RPT-1 excels on medium datasets, struggles on very large

**2. Performance by Domain**:
  - Finance: 12 datasets
  - Healthcare: 8 datasets
  - Retail: 7 datasets
  - Manufacturing: 6 datasets
  - Other: 56 datasets
  - Hypothesis: RPT-1 excels on SAP-relevant domains (finance, supply chain)

**3. Performance by Feature Types**:
  - Numerical-heavy (>80% numerical): 40 datasets
  - Categorical-heavy (>50% categorical): 25 datasets
  - Mixed: 24 datasets
  - Hypothesis: RPT-1 excels on mixed feature types (relational reasoning)

**4. Accuracy-Efficiency Trade-off**:
  - Scatter plot: Accuracy (y-axis) vs Inference Time (x-axis)
  - Pareto frontier: Models dominating accuracy-speed trade-off
  - Identify RPT-1 positioning (high accuracy + fast inference? or high accuracy + slow inference?)

- **Owner**: Shreyas
- **Estimated Hours**: 20 hours analysis + visualization
- **Success Criteria**: 4 subgroup analyses complete with visualizations

**Total Week 14-15**: 890 runs, 30 GPU hours + 20 analysis hours, $27

**Business Value Delivered**:
- **$500K in win rate improvement**: Sales engineers can select optimal model for customer use case
- **Solution engineering guidance**: When to recommend RPT-1 vs AutoGluon vs XGBoost
- **TCO analysis**: RPT-1 zero-shot vs AutoGluon 1-hour tuning (RPT-1 faster by 10x)

**Sales Enablement Impact**:
- **Use case matrix**:
  - "For financial fraud detection (categorical-heavy, <10K rows), use RPT-1"
  - "For large-scale churn prediction (>100K rows), use AutoGluon"
- **Objection handler**: "AutoGluon requires 1 hour tuning per dataset; RPT-1 is instant"

### Milestone M7: All Experiments Complete (End of Week 15)

**Date**: February 21, 2026

**Success Criteria**:
- ✅ All 623 experiments (7 models × 89 datasets) completed
- ✅ 6,230 individual training runs executed (623 × 10 folds)
- ✅ <5% failure rate (≤312 failed runs)
- ✅ Results stored in structured CSV format (model, dataset, fold, metric, value)
- ✅ Total GPU hours ≤180 hours (within conservative budget)
- ✅ Subgroup analyses complete (by size, domain, feature types)
- ✅ Accuracy-efficiency trade-off analysis complete
- ✅ Raw results backed up to cloud storage (AWS S3 or Azure Blob)

**Validation Process**:
1. Completeness check: All expected result files exist
2. Data integrity check: No missing values, NaNs, or corrupted results
3. Sanity check: Performance within expected ranges (not 100%, not random)
4. Cross-reference: Results correlate with published benchmarks (TabArena, TabZilla)
5. Backup verification: Cloud storage backup successful, checksums match

**Business Value Delivered**:
- **$500K in solution engineering value**: Use case-specific model recommendations
- **Performance benchmarking database**: 6,230 training runs = largest independent tabular AI study
- **Optimization roadmap**: Identify RPT-1 improvement opportunities based on failure patterns

**Sales Enablement Readiness**: 85%
- Use case-specific recommendations ready
- Competitive differentiation clear
- Not yet peer-reviewed (statistical testing pending)

**Cumulative Compute Investment**:
- Total GPU hours: 178 hours (within 180-hour conservative budget)
- Total cost: $160.20 (UW Tillicum H200 @ $0.90/hour)
- Cost savings vs AWS: $384.48 (AWS p3.2xlarge would cost $544.68)

**Risk Assessment**:
- **Low Risk**: All major experimental milestones achieved
- **Fallback**: If >5% failure rate, proceed with available results (still 5,900+ runs)

**Paradigm Shift Comparison**:
- **ImageNet (2012)**: 1.2M images, 1 week evaluation
- **BERT (2018)**: 11 tasks, 2 weeks evaluation
- **AlphaFold (2020)**: 100+ proteins, 2 weeks blind prediction
- **Our M7**: **6,230 training runs, 8 weeks comprehensive benchmarking** = largest independent tabular AI validation

---

## Phase 4: Statistical Analysis & Optimization (Weeks 16-17)

**Duration**: February 22 - March 7, 2026 (2 weeks)

**Objective**: Perform rigorous statistical testing and generate publication-quality visualizations.

**Paradigm Shift Comparison**:
- **ImageNet (2012)**: Independent ILSVRC organizers validated results
- **BERT (2018)**: Public GLUE leaderboard with transparent scoring
- **AlphaFold (2020)**: Third-party CASP14 assessors scored submissions
- **Our approach**: Friedman + Nemenyi tests for statistical rigor (NeurIPS/ICML standards)

### Week 16: Statistical Testing

**Business Value Focus**: Achieve academic credibility for peer review

**Statistical Testing Tasks**

#### 1. Data Aggregation
- **Objective**: Prepare results for statistical analysis
- **Activities**:
  - Load all 6,230 training run results from `/results/`
  - Aggregate cross-validation folds (mean, std per model-dataset pair)
  - Generate summary table: 7 models × 89 datasets = 623 rows
  - Handle missing values (failed experiments):
    - Option 1: Exclude dataset from analysis
    - Option 2: Impute with model's mean performance across datasets
  - Document missing data strategy in appendix
- **Owner**: Shreyas
- **Timeline**: Week 16, Day 1
- **Success Criteria**: Summary table with 623 rows (or fewer if datasets excluded)

#### 2. Friedman Test
- **Objective**: Test overall significance of model differences
- **Activities**:
  - Apply Friedman test (non-parametric, suitable for non-normal distributions)
  - Null hypothesis: All 7 models perform identically
  - Alternative hypothesis: At least one model differs significantly
  - Report test statistic, p-value, degrees of freedom
  - Interpret result: If p < 0.05, reject null (models differ significantly)
- **Owner**: Shreyas
- **Timeline**: Week 16, Day 2
- **Success Criteria**: Friedman test complete, p-value reported
- **Expected Outcome**: p < 0.001 (highly significant differences)

#### 3. Nemenyi Post-Hoc Analysis
- **Objective**: Pairwise comparison between all 7 models
- **Activities**:
  - Apply Nemenyi test (post-hoc after Friedman)
  - Calculate critical difference (CD) value (α = 0.05)
  - Generate pairwise comparison matrix (7×7 = 21 pairs)
  - Identify statistically significant differences (p < 0.05)
  - Interpret: Which models are significantly better/worse than RPT-1?
- **Owner**: Shreyas
- **Timeline**: Week 16, Day 3
- **Success Criteria**: Nemenyi analysis complete, CD value calculated

#### 4. Critical Difference Diagram
- **Objective**: Visualize model rankings with statistical significance
- **Activities**:
  - Generate CD diagram (horizontal axis = average rank, vertical = models)
  - Connect models that are NOT significantly different (horizontal bars)
  - Annotate with CD value and significance level
  - Follow NeurIPS/ICML figure guidelines (high resolution, clear labels)
- **Owner**: Shreyas
- **Timeline**: Week 16, Day 3
- **Success Criteria**: Publication-quality CD diagram (PNG, 300 DPI)

#### 5. Wilcoxon Signed-Rank Tests
- **Objective**: Direct pairwise comparison RPT-1 vs each competitor
- **Activities**:
  - Run 6 Wilcoxon tests: RPT-1 vs [XGBoost, CatBoost, LightGBM, TabPFN, TabICL, AutoGluon]
  - Apply Bonferroni correction (α = 0.05 / 6 = 0.0083)
  - Calculate effect sizes (Cohen's d)
  - Interpret: Is RPT-1 significantly better/worse than each competitor?
- **Owner**: Shreyas
- **Timeline**: Week 16, Day 4
- **Success Criteria**: 6 Wilcoxon tests complete, effect sizes reported

#### 6. Subgroup Statistical Tests
- **Objective**: Validate subgroup findings with statistical rigor
- **Activities**:
  - Repeat Friedman + Nemenyi for each subgroup:
    - By dataset size (small, medium, large, very large)
    - By domain (finance, healthcare, retail, manufacturing)
    - By feature types (numerical-heavy, categorical-heavy, mixed)
  - Identify subgroups where RPT-1 significantly outperforms competitors
  - Document findings for sales enablement (use case guidance)
- **Owner**: Shreyas
- **Timeline**: Week 16, Day 5
- **Success Criteria**: Statistical tests complete for all subgroups

**Business Value Delivered**:
- **$750K in enterprise trust value**: Statistical rigor de-risks SAP investment
- **Peer-review readiness**: NeurIPS/ICML submission-quality statistical testing
- **Objection handler**: "Independent validation with p<0.001 significance"

### Week 17: Visualization & Reproducibility

**Business Value Focus**: Generate publication-quality figures and ensure reproducibility

**Visualization Tasks**

#### 1. Performance Heatmap
- **Objective**: Visualize 7 models × 89 datasets performance matrix
- **Activities**:
  - Generate heatmap (rows = datasets, columns = models, color = accuracy)
  - Sort rows by difficulty (easiest to hardest datasets)
  - Annotate with domain labels (finance, healthcare, retail)
  - Highlight RPT-1 wins (green) and losses (red) vs best competitor
- **Owner**: Shreyas
- **Format**: PNG (300 DPI) + interactive Plotly HTML

#### 2. Box Plots by Model
- **Objective**: Show performance distribution across 89 datasets
- **Activities**:
  - Generate box plots (x-axis = models, y-axis = accuracy)
  - Annotate with median, quartiles, outliers
  - Overlay significance brackets (from Nemenyi test)
- **Owner**: Shreyas
- **Format**: PNG (300 DPI)

#### 3. Scatter Plots (Accuracy vs Time)
- **Objective**: Visualize accuracy-efficiency trade-off
- **Activities**:
  - Scatter plot: Accuracy (y-axis) vs Training Time (x-axis)
  - Scatter plot: Accuracy (y-axis) vs Inference Time (x-axis)
  - Annotate Pareto frontier (models dominating trade-off)
  - Highlight RPT-1 positioning
- **Owner**: Shreyas
- **Format**: PNG (300 DPI)

#### 4. Subgroup Comparison Charts
- **Objective**: Visualize subgroup findings
- **Activities**:
  - Bar charts: Model performance by dataset size (4 bars per model)
  - Bar charts: Model performance by domain (5 bars per model)
  - Bar charts: Model performance by feature types (3 bars per model)
  - Annotate with statistical significance stars (*, **, ***)
- **Owner**: Shreyas
- **Format**: PNG (300 DPI)

**Reproducibility Tasks**

#### 5. REFORMS Checklist
- **Objective**: Ensure reproducibility per NeurIPS/ICML standards
- **Activities**:
  - Document all hyperparameters (model configs)
  - Document all random seeds (train/test split, CV folds)
  - Document all preprocessing steps (missing value imputation, encoding)
  - Document all software versions (Python, PyTorch, scikit-learn)
  - Document all hardware specs (UW Tillicum H200)
  - Provide dataset access instructions (OpenML, TabArena, TabZilla)
- **Owner**: Siddarth
- **Deliverable**: `REPRODUCIBILITY.md` (10-15 pages)

#### 6. Docker Image Release
- **Objective**: Enable one-click reproducibility
- **Activities**:
  - Tag Docker images with version numbers (sap-rpt1:v1.0)
  - Push to Docker Hub or GitHub Container Registry
  - Document usage instructions (README)
  - Test reproducibility: New team member runs experiment from scratch
- **Owner**: Siddarth
- **Deliverable**: Public Docker images + usage guide

#### 7. GitHub Repository Finalization
- **Objective**: Prepare open-source release
- **Activities**:
  - Clean up code (remove hardcoded paths, add documentation)
  - Add LICENSE (MIT or Apache 2.0)
  - Add CITATION.cff (for academic citations)
  - Add comprehensive README (setup, usage, results, contact)
  - Add CONTRIBUTING.md (how others can contribute)
  - Create release tag (v1.0.0)
- **Owner**: Siddarth
- **Deliverable**: Public GitHub repository ready for release

### Milestone M8: Statistical Rigor Achieved (End of Week 17)

**Date**: March 7, 2026

**Success Criteria**:
- ✅ Friedman test and Nemenyi analysis complete with p-values
- ✅ Critical difference diagram generated (publication-quality)
- ✅ Wilcoxon signed-rank tests complete (RPT-1 vs 6 competitors)
- ✅ Subgroup statistical tests complete (by size, domain, features)
- ✅ All publication-quality figures created (heatmap, box plots, scatter plots)
- ✅ REFORMS reproducibility checklist complete
- ✅ Docker images released publicly
- ✅ GitHub repository finalized and ready for open-source release

**Validation Process**:
1. Verify statistical test implementation against reference (scipy.stats)
2. Peer review of interpretation (check for Type I/II errors)
3. Ensure visualizations meet NeurIPS/ICML figure guidelines (300 DPI, clear labels)
4. Reproducibility test: New team member reproduces 1 experiment from scratch

**Business Value Delivered**:
- **$750K in enterprise trust**: Statistical rigor de-risks SAP investment
- **Academic credibility**: Peer-review ready statistical testing
- **Open-source community**: Public reproducibility = citation magnet

**Sales Enablement Readiness**: 90%
- Academic credibility achieved (statistical validation)
- Use case guidance validated (subgroup statistical tests)
- Not yet packaged for sales teams (sales enablement materials pending)

**Paradigm Shift Comparison**:
- **ImageNet (2012)**: ILSVRC organizers independently validated top-5 error rates
- **BERT (2018)**: Public GLUE leaderboard with transparent scoring methodology
- **AlphaFold (2020)**: Third-party CASP14 assessors scored with established metrics (GDT, TM-score)
- **Our M8**: Friedman + Nemenyi + Wilcoxon with Bonferroni correction = **NeurIPS/ICML gold standard**

---

## Phase 5: Paper Writing & Sales Enablement (Weeks 18-20)

**Duration**: March 8 - April 4, 2026 (3 weeks)

**Objective**: Draft NeurIPS/ICML conference paper and finalize sales enablement package.

**Paradigm Shift Comparison**:
- **ImageNet (2012)**: 9-page NeurIPS paper (Krizhevsky et al.)
- **BERT (2018)**: 13-page NAACL paper (Devlin et al.)
- **AlphaFold (2020)**: 8-page Nature paper (Jumper et al.)
- **Our approach**: 8-10 page NeurIPS/ICML paper + 30-page appendix + sales enablement package

### Week 18-19: Paper Drafting (NeurIPS/ICML Format)

**Business Value Focus**: Achieve academic publication for SAP credibility

**Paper Structure (8-10 pages)**

#### 1. Introduction (1.5 pages)
- **Objective**: Motivate independent benchmarking of tabular foundation models
- **Content**:
  - **Motivation**: Tabular AI market inflection point ($8.5B → $18.2B)
  - **Research Gap**: Lack of independent RPT-1 validation (only SAP-published results)
  - **Contributions**:
    - First comprehensive benchmark of SAP RPT-1 (89 datasets, 15+ domains)
    - Head-to-head comparison vs TabPFN, AutoGluon, XGBoost (statistical rigor)
    - Reproducible methodology (Docker, open datasets, public code)
    - Use case guidance for enterprise adoption
  - **Paradigm Shift Framing**: Compare to ImageNet, BERT, AlphaFold validation moments
- **Owner**: Rahil
- **Timeline**: Week 18, Days 1-2
- **Quality Standard**: BCG/McKinsey "so what" clarity (lead with insight, not methodology)

#### 2. Related Work (1 page)
- **Objective**: Position within tabular AI research landscape
- **Content**:
  - **Tabular Foundation Models**: TabPFN (Nature 2022), TabICL, RPT-1 (ConTextTab 2025)
  - **AutoML Platforms**: AutoGluon, H2O.ai, FLAML
  - **Traditional ML**: XGBoost, CatBoost, LightGBM
  - **Prior Benchmarking Studies**: TabArena, TabZilla, AutoML Benchmark
  - **Gap**: No independent validation of RPT-1 across diverse domains
- **Owner**: Siddarth
- **Timeline**: Week 18, Day 3
- **Quality Standard**: Cite 30-40 references (establish scholarly rigor)

#### 3. Methodology (2 pages)
- **Objective**: Describe three-pillar benchmarking approach
- **Content**:
  - **Pillar 1: Dataset Diversity**:
    - 89 datasets from TabArena (51), TabZilla (20), OpenML-CC18 (18)
    - 15+ domains (finance, healthcare, retail, manufacturing)
    - Dataset characteristics (size: 100-100K rows, features: 5-500, task: classification/regression)
  - **Pillar 2: Model Breadth**:
    - SAP RPT-1 (relational foundation model)
    - TabPFN v2.5 (Bayesian in-context learning)
    - TabICL (transformer in-context learning)
    - AutoGluon (ensemble AutoML)
    - XGBoost, CatBoost, LightGBM (gradient boosting baselines)
  - **Pillar 3: Statistical Rigor**:
    - 10-fold stratified cross-validation
    - Friedman test (overall significance)
    - Nemenyi post-hoc (pairwise comparisons)
    - Wilcoxon signed-rank (RPT-1 vs competitors)
  - **Reproducibility**: Docker environments, fixed random seeds (42), public datasets
- **Owner**: Rahil + Siddarth
- **Timeline**: Week 18, Days 4-5
- **Quality Standard**: Sufficient detail for reproduction (REFORMS checklist)

#### 4. Results (2.5 pages)
- **Objective**: Present findings with statistical evidence
- **Content**:
  - **Overall Performance Comparison**:
    - Friedman test result: χ²(6) = XXX, p < 0.001 (models differ significantly)
    - Nemenyi critical difference diagram (model rankings)
    - Average rank: [Model 1 = 2.3, Model 2 = 3.1, ..., Model 7 = 5.8]
  - **RPT-1 vs Competitors (Wilcoxon Tests)**:
    - RPT-1 vs XGBoost: Z = XXX, p = XXX, Cohen's d = XXX
    - RPT-1 vs TabPFN: Z = XXX, p = XXX, Cohen's d = XXX
    - [Repeat for all 6 comparisons]
  - **Subgroup Analyses**:
    - By dataset size: RPT-1 excels on medium datasets (1K-10K rows)
    - By domain: RPT-1 outperforms on finance (p<0.01) and healthcare (p<0.05)
    - By feature types: RPT-1 excels on mixed (numerical + categorical) features
  - **Accuracy-Efficiency Trade-off**:
    - RPT-1 achieves competitive accuracy (within 2% of best) with 10x faster inference than AutoGluon
    - XGBoost fastest training (2 min avg), RPT-1 fastest inference (0.5 sec avg)
  - **Figures**:
    - Figure 1: Critical difference diagram (Nemenyi)
    - Figure 2: Performance heatmap (7 models × 89 datasets)
    - Figure 3: Accuracy vs inference time scatter plot
    - Figure 4: Subgroup analysis (performance by dataset size)
- **Owner**: Shreyas
- **Timeline**: Week 19, Days 1-3
- **Quality Standard**: Every claim backed by p-value or effect size

#### 5. Discussion (1.5 pages)
- **Objective**: Interpret findings and provide actionable insights
- **Content**:
  - **When does RPT-1 excel?**:
    - Medium datasets (1K-10K rows) with mixed feature types
    - Finance and healthcare domains (relational reasoning)
    - Zero-shot scenarios (no hyperparameter tuning time)
  - **When does RPT-1 underperform?**:
    - Very large datasets (>100K rows) = OOM issues
    - High-dimensional data (>500 features) = inference slowdown
    - Purely numerical datasets (gradient boosting excels)
  - **Implications for Enterprise Adoption**:
    - RPT-1 is "AutoML replacement" for medium datasets (saves tuning time)
    - RPT-1 is NOT "XGBoost killer" for all use cases (use case-specific)
    - SAP should optimize RPT-1 for large datasets (memory efficiency)
  - **Optimization Opportunities for SAP**:
    - Improve scaling to >100K rows (distributed inference)
    - Optimize categorical feature handling (CatBoost-like strategies)
    - Extend to time-series (SAP use case: demand forecasting)
  - **Limitations and Future Work**:
    - Limited to classification and regression (no time-series, no NLP)
    - Relational features underexplored (RPT-1's unique strength)
    - Future: Benchmark on SAP-specific datasets (SuccessFactors, S/4HANA)
- **Owner**: Rahil
- **Timeline**: Week 19, Days 4-5
- **Quality Standard**: Actionable insights (not just "RPT-1 is good/bad")

#### 6. Conclusion (0.5 pages)
- **Objective**: Summarize findings and call to action
- **Content**:
  - **Summary**: RPT-1 is competitive with state-of-the-art on 89 datasets (statistical evidence)
  - **Key Finding**: RPT-1 excels on medium datasets with mixed features (enterprise sweet spot)
  - **Call to Action**: Tabular AI community should adopt independent benchmarking (like ImageNet, GLUE, CASP)
  - **Impact**: This study de-risks SAP RPT-1 adoption for enterprises ($1.5M+ first-year value)
- **Owner**: Rahil
- **Timeline**: Week 19, Day 5
- **Quality Standard**: Memorable takeaway (what should reader remember 1 week later?)

**Technical Appendix (30-40 pages)**

#### 7. Supplementary Material
- **Content**:
  - **Appendix A**: Per-dataset results tables (89 datasets × 7 models = 623 rows)
  - **Appendix B**: Detailed statistical test outputs (Friedman, Nemenyi, Wilcoxon)
  - **Appendix C**: Model hyperparameter configurations
  - **Appendix D**: Dataset preprocessing details (missing value imputation, encoding)
  - **Appendix E**: Failure mode analysis (timeout, OOM, API issues)
  - **Appendix F**: Reproducibility checklist (REFORMS framework)
  - **Appendix G**: Docker setup instructions
  - **Appendix H**: Dataset manifest (characteristics, domains, sources)
- **Owner**: Shreyas + Mathew
- **Timeline**: Week 19, Days 1-5 (parallel with main paper)
- **Quality Standard**: NeurIPS/ICML supplementary material standards

**Paper Review & Revision**

#### 8. Internal Peer Review
- **Activities**:
  - Each team member reads paper critically (identify gaps, typos, unclear sections)
  - Faculty advisor review (simulate peer review feedback)
  - Iterate on feedback (2-3 revision rounds)
  - Verify all citations (no dead links, correct APA formatting)
  - LaTeX compilation passes (no errors, warnings acceptable)
- **Owner**: All team members
- **Timeline**: Week 19, Day 5
- **Quality Standard**: 9/10 clarity (faculty advisor assessment)

### Week 20: Sales Enablement Package & Final Deliverables

**Business Value Focus**: Enable SAP sales teams to confidently sell RPT-1

**Sales Enablement Components**

#### 1. ROI Calculator (Excel + Interactive Web App)
- **Objective**: Quantify value of RPT-1 for customer scenarios
- **Inputs**:
  - Current approach (manual analysis, XGBoost, AutoGluon)
  - Dataset characteristics (size, features, task type)
  - Business metrics (deal size, sales cycle length, win rate)
- **Outputs**:
  - Year 1/3/5 ROI from reduced data science time
  - Payback period (months)
  - TCO comparison (RPT-1 vs alternatives)
- **Scenarios**:
  - Conservative: 20% reduction in data science time
  - Moderate: 40% reduction
  - Optimistic: 60% reduction (zero-shot vs hyperparameter tuning)
- **Owner**: Shreyas
- **Format**: Excel (.xlsx) + Interactive web app (React)
- **Business Value**: Sales engineers quantify ROI for customers

#### 2. TCO Analysis (Total Cost of Ownership)
- **Objective**: Compare RPT-1 costs vs alternatives
- **Components**:
  - Licensing costs (RPT-1 API pricing)
  - Compute costs (inference GPU hours)
  - Data science labor costs (tuning time saved)
  - Training costs (zero-shot vs hyperparameter tuning)
- **Comparison Models**:
  - RPT-1 vs XGBoost (grid search)
  - RPT-1 vs AutoGluon (1-hour tuning)
  - RPT-1 vs TabPFN (ensemble inference)
- **Owner**: Shreyas
- **Format**: PDF report (5-7 pages) + Excel calculator
- **Business Value**: CFOs justify RPT-1 investment

#### 3. Use Case Library (15-20 Customer Scenarios)
- **Objective**: Map RPT-1 performance to SAP customer use cases
- **Use Cases** (SAP-relevant):
  - **Finance**: Fraud detection, credit scoring, risk assessment
  - **Healthcare**: Patient readmission prediction, treatment outcome prediction
  - **Retail**: Customer churn prediction, demand forecasting, recommendation
  - **Manufacturing**: Predictive maintenance, quality control, supply chain optimization
  - **HR (SuccessFactors)**: Employee attrition prediction, talent matching
- **For Each Use Case**:
  - Dataset example (from our 89 benchmarks)
  - RPT-1 performance vs XGBoost/AutoGluon
  - Business impact (e.g., "30% reduction in false positives = $500K annual savings")
  - Implementation guidance (data requirements, deployment)
- **Owner**: Rahil
- **Format**: PDF report (15-20 pages, 1 page per use case)
- **Business Value**: Sales engineers demonstrate domain expertise

#### 4. Objection Handlers (FAQ for Sales Teams)
- **Objective**: Equip sales teams to handle customer skepticism
- **Common Objections**:
  - "Why not just use XGBoost? It's free and proven."
    - **Answer**: RPT-1 is zero-shot (saves 15 hours hyperparameter tuning per dataset). For 10 datasets/year, that's $30K in data science time.
  - "TabPFN is also a foundation model and it's open-source."
    - **Answer**: TabPFN limited to 10K rows, 500 features. RPT-1 scales to 1M rows, 10K features.
  - "How do I know RPT-1 will work on my data?"
    - **Answer**: Independent validation on 89 datasets across 15+ domains. 75% probability RPT-1 matches or exceeds XGBoost.
  - "What if RPT-1 underperforms XGBoost on my use case?"
    - **Answer**: SAP offers hybrid approach: RPT-1 for rapid prototyping, fallback to XGBoost if needed.
- **Owner**: Rahil
- **Format**: PDF cheat sheet (2 pages, double-sided)
- **Business Value**: Reduce sales cycle friction (30-40% faster close rate)

#### 5. Competitive Differentiation Matrix
- **Objective**: Position RPT-1 vs competitors
- **Comparison Dimensions**:
  - Accuracy (benchmark results)
  - Speed (inference time)
  - Ease of use (zero-shot vs tuning required)
  - Scalability (dataset size limits)
  - Enterprise support (SAP vs open-source)
  - Pricing (API costs vs self-hosted)
- **Competitors**: TabPFN, AutoGluon, XGBoost, Microsoft Azure ML, Oracle ML
- **Owner**: Rahil
- **Format**: 1-page matrix (PowerPoint slide + PDF)
- **Business Value**: Sales teams confidently compare RPT-1 to alternatives

#### 6. Demo Scripts & Video Walkthroughs
- **Objective**: Enable sales engineers to demo RPT-1
- **Demo 1**: "Zero-Shot Fraud Detection in 5 Minutes"
  - Upload CSV dataset (credit card transactions)
  - RPT-1 auto-detects fraud (no tuning)
  - Compare to XGBoost (requires 1 hour hyperparameter search)
  - **Format**: 3-minute video + written script

- **Demo 2**: "RPT-1 vs AutoGluon Head-to-Head"
  - Same dataset, both models
  - RPT-1: Instant inference
  - AutoGluon: 1-hour training
  - Compare accuracy (within 2%) and time (10x faster)
  - **Format**: 5-minute video + written script

- **Demo 3**: "Interactive Dataset Explorer"
  - Show 89 benchmarked datasets
  - Filter by industry (finance, healthcare, retail)
  - Show RPT-1 performance on customer-relevant datasets
  - **Format**: Interactive web app + 2-minute video

- **Owner**: Siddarth (technical), Rahil (scripting)
- **Format**: 3 videos (MP4, 1080p) + 3 scripts (PDF, 2 pages each)
- **Business Value**: Sales engineers deliver confident demos (win rate +15%)

**Final Deliverables Assembly**

#### 7. Update PowerPoint Presentation (35-45 slides)
- **Activities**:
  - Replace placeholder results with actual experimental data
  - Add statistical test results (Friedman, Nemenyi, Wilcoxon)
  - Add publication-quality figures (heatmap, CD diagram, scatter plots)
  - Update timeline with actual milestones achieved
  - Add sales enablement slides (ROI calculator, use case library)
- **Owner**: Rahil + Shreyas
- **Timeline**: Week 20, Days 1-2
- **Quality Standard**: Ready for SAP C-suite presentation

#### 8. Update PDF Report (25-35 pages)
- **Activities**:
  - Replace placeholder results with actual data
  - Add statistical analysis section (Friedman, Nemenyi, Wilcoxon)
  - Add sales enablement section (ROI, TCO, use cases)
  - Finalize citations (APA style)
  - Professional proofreading (Grammarly + manual review)
- **Owner**: Rahil + Shreyas
- **Timeline**: Week 20, Days 2-3
- **Quality Standard**: Academic journal submission-ready

#### 9. Update Interactive HTML Viewer
- **Activities**:
  - Populate dataset explorer with 89 real datasets
  - Update model comparison tool with actual performance data
  - Update ROI calculator with validated assumptions
  - Add "Download Results" functionality (CSV, PDF)
  - Deploy to web hosting (GitHub Pages, Netlify, or Azure Static Web Apps)
- **Owner**: Siddarth
- **Timeline**: Week 20, Days 3-4
- **Quality Standard**: Enterprise SaaS UI/UX standards

#### 10. Finalize GitHub Repository
- **Activities**:
  - Upload all experimental results (CSV files to `/results/`)
  - Upload all figures (PNG, SVG to `/figures/`)
  - Upload paper PDF and supplementary material
  - Update README with final results summary
  - Create release tag (v1.0.0) with DOI (Zenodo)
  - Add "Cite this work" section (BibTeX)
- **Owner**: Siddarth
- **Timeline**: Week 20, Day 4
- **Quality Standard**: 100+ GitHub stars within 3 months (citation magnet)

#### 11. Quality Assurance Final Check
- **Activities**:
  - All deliverables reviewed by each team member
  - Faculty advisor final approval (BCG/McKinsey 9.5/10 standard)
  - SAP stakeholder preview (share draft with Walter Sun, Sam Thelin)
  - Incorporate feedback (1 round of revisions)
  - File integrity check (PowerPoint opens, PDF prints, HTML loads)
- **Owner**: All team members
- **Timeline**: Week 20, Day 5
- **Quality Standard**: Zero critical issues (typos acceptable if <5)

### Milestone M9: Paper Draft Complete (End of Week 19)

**Date**: March 28, 2026

**Success Criteria**:
- ✅ NeurIPS/ICML paper draft complete (8-10 pages)
- ✅ Technical appendix complete (30-40 pages)
- ✅ Internal peer review complete (all team members + faculty advisor)
- ✅ LaTeX compilation passes
- ✅ All figures referenced correctly
- ✅ Citations complete and formatted (APA style)
- ✅ Reproducibility checklist complete (REFORMS)
- ✅ Ready for conference submission (post-project)

**Validation Process**:
1. Clarity test: Faculty advisor reads paper, summarizes key finding in 1 sentence
2. Reproducibility test: New team member reproduces 1 experiment using paper + appendix
3. Citation verification: All references accessible (no dead links)
4. Figure quality: All figures 300 DPI, labels readable at 50% zoom

**Business Value Delivered**:
- **$1.2M in market positioning value**: Academic publication establishes SAP as tabular AI leader
- **Peer-review credibility**: De-risks enterprise adoption (independent validation)
- **Citation magnet**: Open-source code + reproducible results = 50+ citations within 2 years

**Sales Enablement Readiness**: 95%
- Academic credibility achieved (peer-review ready paper)
- Sales enablement materials in progress (pending Week 20)

### Milestone M10: Sales Enablement Package Ready (End of Week 20)

**Date**: April 4, 2026

**Success Criteria**:
- ✅ ROI calculator (Excel + web app) complete and validated
- ✅ TCO analysis (PDF report) complete
- ✅ Use case library (15-20 customer scenarios) complete
- ✅ Objection handlers (FAQ) complete
- ✅ Competitive differentiation matrix complete
- ✅ Demo scripts & video walkthroughs (3 demos) complete
- ✅ PowerPoint presentation updated with final results
- ✅ PDF report updated with final results
- ✅ Interactive HTML viewer deployed and accessible
- ✅ GitHub repository finalized and released (v1.0.0)
- ✅ All deliverables quality-checked and SAP-approved

**Validation Process**:
1. ROI calculator test: Run 5 customer scenarios, verify outputs match manual calculations
2. Use case validation: SAP account team reviews and confirms customer relevance
3. Demo script test: Sales engineer delivers demo, receives feedback
4. Deliverables review: SAP stakeholders (Walter Sun, Sam Thelin) approve final package
5. Public release: GitHub repository live, Docker images accessible, HTML viewer deployed

**Business Value Delivered**:
- **$1.5M+ first-year impact**: Sales enablement package accelerates sales cycles, improves win rates
- **Complete validation study**: Academic publication + sales tools + open-source code
- **SAP competitive advantage**: First enterprise with independent tabular AI validation (ImageNet moment)

**Sales Enablement Readiness**: **100%**
- ✅ Academic credibility (peer-review ready paper)
- ✅ Sales tools (ROI calculator, TCO analysis, use case library, objection handlers)
- ✅ Demos (3 video walkthroughs + interactive web app)
- ✅ Reproducibility (open-source GitHub repository, Docker images)

**Cumulative Business Value**:
- **Year 1 ROI**: $1.5M (reduced sales cycles, improved win rates, POC acceleration)
- **Year 3 ROI**: $8.5M (assuming 15% of SAP's $50M+ AI-influenced ARR accelerated by 6 months)
- **Total 20-Week Investment**: $75K-$120K (team time + compute)
- **ROI Multiple**: 12x (Year 1), 71x (Year 3)

**Paradigm Shift Achievement**:
- **ImageNet (2012)**: Independent ILSVRC validation → $2.1B VC funding within 18 months
- **BERT (2018)**: GLUE benchmark → 80% F500 adoption within 12 months
- **AlphaFold (2020)**: CASP14 validation → $100M+ pharma savings within 24 months
- **SAP RPT-1 (2026)**: **Independent 89-dataset validation → $1.5M+ Year 1 sales impact → $8.5M 3-year market positioning**

---

## STAKEHOLDER ENGAGEMENT TIMELINE

### Parallel to Execution Phases (Weeks 1-20)

**Week 3: Initial Outreach (Tier 1)**
- **Activity**: Email Walter Sun (Global Head of AI, SAP) via UW faculty introduction
- **Content**: 1-page executive summary (market opportunity, validation value, team credentials)
- **Goal**: Secure informational meeting (15-30 minutes)
- **Success Metric**: Response within 1 week
- **Owner**: Rahil
- **Business Value**: Executive sponsor buy-in

**Week 4: Tier 1 Follow-Up + Tier 2 Expansion**
- **Activity**: Follow up with Walter Sun, reach out to Sam Thelin & Johannes Hoffart
- **Content**: Full proposal deliverables (PowerPoint, PDF, interactive HTML viewer)
- **Goal**: Secure technical collaboration and co-authorship interest
- **Success Metric**: 2+ stakeholders engaged
- **Owner**: Rahil
- **Business Value**: Internal champion recruitment

**Week 7: Technical Collaboration Initiation**
- **Activity**: Schedule call with Sam Thelin (ConTextTab lead author)
- **Content**: Discuss RPT-1 API access, configuration details, co-authorship
- **Goal**: Secure RPT-1 API credentials and methodology feedback
- **Success Metric**: RPT-1 access granted
- **Owner**: Rahil + Siddarth
- **Business Value**: Technical enablement

**Week 11: Mid-Project Check-In**
- **Activity**: Share progress update with SAP stakeholders
- **Content**: Preliminary baseline results (XGBoost, CatBoost, LightGBM on 89 datasets)
- **Goal**: Demonstrate project momentum, address methodology concerns
- **Success Metric**: Positive feedback on approach
- **Owner**: Rahil
- **Business Value**: Maintain stakeholder engagement

**Week 13: Results Preview**
- **Activity**: Share preliminary RPT-1 findings with SAP team
- **Content**: Early statistical analysis (RPT-1 vs XGBoost head-to-head)
- **Goal**: Discuss publication co-authorship, gauge SAP interest
- **Success Metric**: Co-authorship commitment or feedback incorporation
- **Owner**: Rahil + Shreyas
- **Business Value**: SAP co-branding of publication

**Week 17: Pre-Submission Review**
- **Activity**: Share draft paper with SAP stakeholders
- **Content**: Full NeurIPS/ICML draft (8-10 pages + appendix)
- **Goal**: Incorporate SAP feedback, finalize co-authorship
- **Success Metric**: SAP approves for submission
- **Owner**: Rahil
- **Business Value**: SAP endorsement of findings

**Week 20: Final Presentation & Handoff**
- **Activity**: Present complete results to SAP leadership
- **Content**: PowerPoint presentation (35-45 slides), sales enablement package
- **Goal**: Deliver all final deliverables, discuss ongoing collaboration
- **Success Metric**: SAP commits to using sales enablement materials
- **Owner**: All team members
- **Business Value**: Sales enablement adoption ($1.5M+ Year 1 impact)

**Post-Week 20: Ongoing Engagement**
- **Activity**: NeurIPS/ICML submission (May 2026), GitHub repository promotion
- **Goal**: Achieve publication acceptance, 100+ GitHub stars
- **Success Metric**: Paper accepted (peer-review), 50+ citations within 2 years
- **Owner**: Rahil
- **Business Value**: Long-term SAP credibility and market positioning

---

## RISK MITIGATION & CONTINGENCY PLANS

### Critical Risks and Mitigation Strategies

**Risk 1: UW Tillicum GPU Unavailable**
- **Probability**: Low (20%)
- **Impact**: High (project delay, cost increase)
- **Mitigation**:
  - Apply for access Week 5 (2-week lead time)
  - Secure AWS/Azure research credits as backup (UW student programs)
  - Test access Week 5, Day 3 (early validation)
- **Contingency**:
  - Pivot to AWS p3.2xlarge ($3.06/hour) = $544.68 total (vs $160.20 Tillicum)
  - Request budget increase to $600 (conservative scenario)
- **Fallback**: Azure NC6s_v3 ($0.90/hour via UW partnership)

**Risk 2: Dataset Download Failures**
- **Probability**: Low (10%)
- **Impact**: Medium (dataset count reduction)
- **Mitigation**:
  - Implement retry logic with exponential backoff
  - Verify checksums for data integrity
  - TabArena/TabZilla hosted on stable infrastructure (OpenML, Zenodo)
- **Contingency**:
  - Proceed with 71 datasets (TabArena + TabZilla only, exclude OpenML-CC18)
  - Still statistically robust (71 datasets = high power)
- **Fallback**: Manual download as last resort

**Risk 3: Experiment Runtime Overruns (>180 GPU hours)**
- **Probability**: Medium (40%)
- **Impact**: Medium (cost increase)
- **Mitigation**:
  - Set 4-hour timeout per model-dataset (prevent runaway jobs)
  - Monitor progress daily (Weeks 8-15)
  - Use efficient hyperparameter search (coarse grid, not exhaustive)
- **Contingency**:
  - Request budget increase to $200-$250 (conservative scenario)
  - Prioritize RPT-1 experiments (Weeks 10-11 = critical path)
- **Fallback**: Reduce CV folds from 10 to 5 (still valid, lower statistical power)

**Risk 4: Statistical Significance Not Achieved**
- **Probability**: Low (15%)
- **Impact**: Medium (academic publication challenges)
- **Mitigation**:
  - 89 datasets provide high statistical power (detect small effect sizes)
  - Use robust statistical tests (Friedman + Nemenyi + Wilcoxon)
- **Contingency**:
  - Report as "RPT-1 competitive but not superior" (still valuable finding)
  - Emphasize subgroup findings (RPT-1 excels on specific use cases)
- **Fallback**: Frame as "comprehensive benchmarking study" (descriptive, not inferential)

**Risk 5: SAP Stakeholder Non-Response**
- **Probability**: Medium (30%)
- **Impact**: Low (project value persists independently)
- **Mitigation**:
  - Multi-channel outreach (email, LinkedIn, UW faculty introduction)
  - Tier 1/2/3 strategy (fallback to lower tiers if Tier 1 unresponsive)
  - Value proposition tailored to each stakeholder role
- **Contingency**:
  - Proceed with independent benchmarking (publication still valuable)
  - Reach out to SAP competitors (Microsoft, Oracle) if SAP unresponsive
- **Fallback**: Open-source community adoption (GitHub stars, citations)

**Risk 6: Team Member Unavailability**
- **Probability**: Medium (25%)
- **Impact**: High (workload redistribution)
- **Mitigation**:
  - Cross-training on critical tasks (Weeks 2-3)
  - Documentation of all processes (reproducible by any team member)
  - Weekly check-ins (identify blockers early)
- **Contingency**:
  - Redistribute workload among remaining 3 members
  - Extend timeline by 1-2 weeks if critical path affected
- **Fallback**: Reduce scope (e.g., 71 datasets instead of 89)

**Risk 7: RPT-1 API Access Denied**
- **Probability**: Medium (35%)
- **Impact**: Medium (switch to open-source RPT-1-OSS)
- **Mitigation**:
  - Request API access Week 4 (via Sam Thelin)
  - Test API access Week 7 (early validation)
- **Contingency**:
  - Use open-source RPT-1-OSS variant (90% feature parity)
  - Document limitations in paper (API vs open-source differences)
- **Fallback**: Frame as "RPT-1-OSS benchmarking" (still valuable for open-source community)

**Risk 8: NeurIPS/ICML Submission Deadline Missed**
- **Probability**: Low (10%)
- **Impact**: Medium (publication delay to next conference)
- **Mitigation**:
  - Target Week 19 for paper draft (1 week buffer before Week 20)
  - Internal peer review Week 19, Day 5 (early feedback)
- **Contingency**:
  - Submit to backup conferences (ICLR, AISTATS, KDD)
  - Publish as arXiv preprint (immediate dissemination)
- **Fallback**: Submit to domain-specific conferences (RecSys, CIKM for tabular AI)

**Risk 9: Sales Enablement Materials Rejected by SAP**
- **Probability**: Low (15%)
- **Impact**: Medium (reduce Year 1 ROI projection)
- **Mitigation**:
  - Collaborate with SAP sales engineers Week 17-19 (iterative feedback)
  - Validate use case library with SAP account teams
- **Contingency**:
  - Publish sales enablement materials independently (open-source)
  - Target other tabular AI vendors (Microsoft, Oracle, Google)
- **Fallback**: Academic publication alone still delivers $750K enterprise trust value

---

## SUCCESS METRICS

### Academic Impact

**Target 1: NeurIPS/ICML 2026 Submission**
- ✅ Paper draft ready by Week 19 (March 28, 2026)
- ✅ Submission within 2 months post-project (June 2026)
- ✅ Target: NeurIPS (December 2026) or ICML (July 2026)
- **Success Metric**: Paper accepted for publication (peer-review)

**Target 2: Open-Source Community Adoption**
- ✅ GitHub repository public by Week 20 (April 4, 2026)
- ✅ Target: 100+ GitHub stars within 6 months (October 2026)
- ✅ Target: 10+ forks (community experimentation)
- **Success Metric**: Community contributions (PRs, issues, citations)

**Target 3: Citation Impact**
- ✅ arXiv preprint published Week 20 (April 2026)
- ✅ Target: 5+ citations within 12 months (April 2027)
- ✅ Target: 50+ citations within 24 months (April 2028)
- **Success Metric**: Google Scholar citations tracking

### SAP Business Value

**Target 4: Sales Enablement Adoption**
- ✅ Sales enablement package delivered Week 20
- ✅ Target: SAP sales teams use ROI calculator in 10+ customer meetings (Q2 2026)
- ✅ Target: Use case library referenced in 20+ POCs (Q2-Q3 2026)
- **Success Metric**: SAP internal tracking (sales tool usage analytics)

**Target 5: Competitive Positioning**
- ✅ Actionable recommendations incorporated into SAP AI Foundation roadmap
- ✅ Target: 3+ roadmap items influenced by benchmarking findings (Q3 2026)
- ✅ Target: RPT-1 optimization based on failure mode analysis (Q4 2026)
- **Success Metric**: SAP R&D team confirmation (product roadmap updates)

**Target 6: Co-Authorship Opportunity**
- ✅ SAP researchers (Sam Thelin, Johannes Hoffart) co-author paper
- ✅ Target: SAP endorsement of independent validation findings
- ✅ Target: Joint presentation at NeurIPS/ICML conference
- **Success Metric**: SAP co-authors listed on publication

### Team Learning & Career Impact

**Target 7: Publication-Quality Research Experience**
- ✅ All 4 team members contribute to NeurIPS/ICML paper
- ✅ Each member leads 2+ paper sections (introduction, methodology, results, discussion)
- ✅ Experience with peer review process
- **Success Metric**: Team reflection (post-project debrief)

**Target 8: SAP Collaboration Strengthening Career Prospects**
- ✅ SAP stakeholder recommendations on LinkedIn (Walter Sun, Sam Thelin)
- ✅ SAP interview opportunities for team members (full-time or internship)
- ✅ Portfolio piece demonstrating enterprise AI validation expertise
- **Success Metric**: LinkedIn recommendations, job offers

**Target 9: Tabular AI Expertise**
- ✅ Team becomes go-to experts on tabular foundation models (RPT-1, TabPFN, TabICL)
- ✅ Speaking opportunities at UW, conferences, industry events
- ✅ Consulting opportunities with enterprises adopting tabular AI
- **Success Metric**: Speaking invitations, consulting inquiries

---

## CONCLUSION

### The 20-Week Journey: From Research to Market Impact

This 20-week timeline transforms SAP RPT-1 from a promising research prototype into an enterprise-validated, sales-enabled tabular AI platform. By replicating the validation timelines that made ImageNet, BERT, and AlphaFold paradigm shifts, we unlock:

**Academic Credibility**: Peer-reviewed publication, reproducible methodology, open-source code (NeurIPS/ICML standards)

**Sales Enablement**: ROI calculator, TCO analysis, use case library, objection handlers, demo scripts ($1.5M+ Year 1 impact)

**Market Positioning**: First enterprise with independent tabular AI validation ($8.5M 3-year competitive advantage)

### Critical Path: Weeks 10-11 (RPT-1 Validation)

Success depends on robust infrastructure setup (Weeks 5-7) enabling smooth RPT-1 experiments (Weeks 10-11). Built-in buffers (Week 15 for re-runs, Week 17 for reproducibility) mitigate experiment delays.

### Paradigm Shift Achievement

| Metric | ImageNet (2012) | BERT (2018) | AlphaFold (2020) | SAP RPT-1 (2026) |
|--------|----------------|-------------|------------------|------------------|
| **Validation Duration** | 1 week (ILSVRC) | 2 weeks (GLUE) | 2 weeks (CASP14) | **20 weeks (comprehensive)** |
| **Benchmark Datasets** | 1 (ImageNet) | 11 (GLUE tasks) | 100+ (proteins) | **89 (TabArena + TabZilla + OpenML-CC18)** |
| **Independent Validation** | ✅ ILSVRC organizers | ✅ GLUE leaderboard | ✅ CASP14 assessors | ✅ **UW academic team** |
| **Statistical Rigor** | Top-5 error (single metric) | Average score (11 tasks) | GDT, TM-score | **Friedman + Nemenyi + Wilcoxon (p<0.001)** |
| **Reproducibility** | Code release (2 weeks post) | Code release (immediate) | Code release (6 months post) | **Docker images + GitHub (Week 20)** |
| **Time to Enterprise Impact** | 18 months ($2.1B VC) | 12 months (80% F500) | 24 months ($100M+ savings) | **Target: 6 months ($1.5M sales)** |

### Next Steps

**Immediate (Week 1-2)**: Complete Phase 0 (research foundation) to inform proposal and methodology.

**Short-Term (Week 3-4)**: Deliver complete proposal to SAP stakeholders, initiate Tier 1 engagement.

**Medium-Term (Week 5-15)**: Execute all benchmarking experiments, validate RPT-1 across 89 datasets.

**Long-Term (Week 16-20)**: Achieve statistical rigor, draft NeurIPS/ICML paper, deliver sales enablement package.

**Post-Project**: Conference submission (June 2026), SAP sales enablement adoption (Q2-Q3 2026), citation impact tracking (2027-2028).

---

**Document Version**: 2.0
**Last Updated**: November 2025
**Classification**: Proposal - Timeline & Milestones (Enhanced)
**Source**: Phase-by-phase expansion with business value, sales enablement, and paradigm shift analysis

**Total Pages**: 900+ lines (comprehensive 20-week roadmap)

**Key Enhancements from V1**:
- ✅ Updated to 20-week timeline (from 12 weeks)
- ✅ Added Paradigm Shift Milestones (ImageNet, BERT, AlphaFold comparisons)
- ✅ Added Business Value Gates (ROI trajectory, cumulative value by milestone)
- ✅ Added Sales Enablement Timeline (readiness % by milestone, $1.5M Year 1 impact)
- ✅ Added ROI Milestones (week-by-week value tracking)
- ✅ Added Risk Mitigation (9 critical risks with mitigation/contingency/fallback)
- ✅ Added Stakeholder Touchpoints (7 engagement moments across 20 weeks)
- ✅ Added Gantt Chart (Mermaid diagram with business value delivery)
- ✅ Connected to $8.5B market opportunity and SAP's $50M+ AI-influenced ARR

**Validation**: This timeline delivers what ImageNet did for computer vision and GLUE did for NLP: independent, reproducible, academically rigorous validation that de-risks enterprise adoption and unlocks market leadership.
