# SAP RPT-1 Benchmarking Study
## Timeline & Milestones

**Project Duration**: 12 weeks (November 8, 2025 - January 31, 2026)

**Total Phases**: 6 major phases from proposal to paper publication

**Target Completion**: NeurIPS/ICML 2026 paper draft ready by Week 12

---

## Timeline Overview

| Phase | Weeks | Duration | Primary Focus | Key Deliverable |
|-------|-------|----------|---------------|-----------------|
| **Phase 0** | 1-2 | 2 weeks | Research & Intelligence | Research foundation complete |
| **Phase 1** | 3-4 | 2 weeks | Proposal Development | Proposal delivered to SAP |
| **Phase 2** | 4-5 | 2 weeks | Infrastructure & Datasets | 70+ datasets ready, codebase initialized |
| **Phase 3** | 6-10 | 5 weeks | Benchmarking Experiments | All experimental runs complete |
| **Phase 4** | 11 | 1 week | Statistical Analysis | Friedman/Nemenyi tests complete |
| **Phase 5** | 12 | 1 week | Paper Writing | NeurIPS/ICML draft ready |

**Total**: 12 weeks from project start to conference submission

---

## Phase 0: Research & Intelligence (Weeks 1-2)

**Duration**: November 8 - November 22, 2025 (2 weeks)

**Objective**: Build comprehensive research foundation and stakeholder intelligence to inform proposal and methodology.

### Week 1: Deep Research

**Tasks**:
1. **SAP Company & Product Intelligence**
   - Research SAP AI Foundation organizational structure
   - Analyze ConTextTab paper (Spinaci et al., 2025) in depth
   - Identify SAP RPT-1 technical specifications and claims
   - Document SAP's competitive landscape positioning
   - **Owner**: Rahil (Product Lead)
   - **Deliverable**: `sap-company-intelligence.md`

2. **Tabular ML Landscape Analysis**
   - Survey competing tabular foundation models (TabPFN, TabICL)
   - Analyze AutoML platforms (AutoGluon, H2O.ai)
   - Document traditional ML baselines (XGBoost, CatBoost, LightGBM)
   - Identify performance benchmarks from literature
   - **Owner**: Siddarth (Technical Lead)
   - **Deliverable**: `tabular-ml-landscape.md`

3. **Benchmarking Methodology Research**
   - Study Friedman test and Nemenyi post-hoc analysis
   - Review REFORMS checklist for ML reproducibility
   - Analyze prior benchmarking papers (TabPFN Nature paper, TabZilla)
   - Define statistical testing protocols
   - **Owner**: Shreyas (Analytics Lead)
   - **Deliverable**: `benchmarking-methodology.md`

4. **Dataset & Benchmark Research**
   - Catalog TabArena datasets (51 datasets)
   - Catalog TabZilla datasets (20 "hardest" datasets)
   - Document dataset characteristics (size, features, domain, task type)
   - Verify dataset availability and licenses
   - **Owner**: Mathew (Data Lead)
   - **Deliverable**: `datasets-benchmarks.md`

### Week 2: Stakeholder Mapping & Planning

**Tasks**:
5. **Stakeholder Intelligence**
   - Map SAP AI Foundation organizational structure
   - Identify key contacts (Walter Sun, Sam Thelin, Johannes Hoffart)
   - Research stakeholder backgrounds (LinkedIn, publications)
   - Define tier 1/2/3 stakeholder prioritization
   - **Owner**: Rahil
   - **Deliverable**: `sap-organizational-structure.md`, `sap-rpt1-product-team.md`

6. **Value Proposition Development**
   - Craft role-specific value propositions (executive, research, product)
   - Define engagement strategy per stakeholder tier
   - Develop email templates and outreach playbook
   - **Owner**: Rahil
   - **Deliverable**: `value-propositions-by-role.md`, `outreach-playbook.md`

7. **Compute Resource Planning**
   - Research UW Tillicum GPU specs and pricing ($0.90/hour)
   - Explore AWS/Azure research credits as backup
   - Estimate compute hours for 3 scenarios (optimistic, moderate, conservative)
   - **Owner**: Mathew
   - **Deliverable**: `compute-resources-guide.md`

8. **Team-Project Matching**
   - Query Knowledge Graph API for team member data
   - Calculate match scores for SAP benchmarking project requirements
   - Assign project roles based on expertise alignment
   - **Owner**: Shreyas
   - **Deliverable**: `team-matching.md`, `shared-data.json`

### Milestone M1: Research Foundation Complete (End of Week 2)

**Success Criteria**:
- All 8 research files completed and validated
- `shared-data.json` created with team and project data
- Stakeholder intelligence ready for outreach
- Methodology framework defined

**Validation**:
- Peer review of all research files by team
- Cross-reference citations and data sources
- Verify no knowledge gaps blocking proposal writing

---

## Phase 1: Proposal Development (Weeks 3-4)

**Duration**: November 23 - December 6, 2025 (2 weeks)

**Objective**: Create complete proposal deliverables (PowerPoint, PDF, HTML) for SAP stakeholders.

### Week 3: Content & Visuals (Parallel Execution)

**Agent 1 Tasks (Content Generator)**:
1. Create 7 markdown content files:
   - Executive Summary (2 pages)
   - Problem Statement (5-7 pages, SCR framework)
   - Methodology (8-12 pages, Three Pillars)
   - Team Presentation (6-8 pages, 100% KG data)
   - Timeline & Milestones (5-7 pages)
   - Expected Outcomes (5-7 pages)
   - Stakeholder Strategy (5-7 pages)
2. Convert all markdown to Word documents (.docx)
   - **Owner**: Agent 1 (Rahil oversight)
   - **Deliverable**: 7 MD + 7 DOCX files

**Agent 2 Tasks (Visual Designer)**:
1. Create 21 visual assets:
   - 6 infographics (model comparison, dataset diversity, timeline, ROI, team structure, competitive landscape)
   - 6 charts (performance heatmap, statistical testing, compute cost, citation network, use case matrix, accuracy-efficiency trade-off)
   - 6 diagrams (three-pillar methodology, experimental workflow, Docker architecture, statistical testing flow, stakeholder map, data pipeline)
   - 3 brand assets (cover page, section dividers, footer template)
   - **Owner**: Agent 2 (Shreyas oversight)
   - **Deliverable**: 21 PNG/SVG files in `/visuals/`

**Agent 3 Tasks (Interactive Developer)**:
1. Create 5 interactive elements:
   - Dataset explorer (interactive table with filters)
   - Model comparison tool (side-by-side feature comparison)
   - Timeline Gantt chart (interactive week-by-week view)
   - ROI calculator (input cost scenarios, see projected outcomes)
   - Team contact directory (with links to profiles)
   - **Owner**: Agent 3 (Siddarth oversight)
   - **Deliverable**: 5 HTML/JS components

**Agent 4 Tasks (Code Repository Setup - Parallel)**:
1. Initialize GitHub repository structure
2. Create Docker base environment
3. Implement dataset download script
4. Build model wrapper templates (RPT-1, TabPFN, AutoGluon, XGBoost)
   - **Owner**: Agent 4 (Siddarth lead)
   - **Deliverable**: GitHub repo with initial codebase

### Week 4: Assembly & Delivery

**Agent 5 Tasks (GitHub Projects)**:
1. Create 150+ GitHub Project tasks spanning Weeks 5-12
2. Set up project boards (To Do, In Progress, Done)
3. Define dependencies and critical path
4. Export timeline to CSV/JSON
   - **Owner**: Agent 5 (Shreyas lead)
   - **Deliverable**: GitHub Projects configured, timeline export

**Final Assembly**:
1. Integrate content + visuals + interactive elements
2. Generate PowerPoint (35-45 slides)
3. Generate PDF report (25-35 pages)
4. Generate Technical Appendix (30-40 pages)
5. Build interactive HTML viewer (COMPLETE_PROPOSAL_VIEWER.html)
6. Quality assurance and validation
   - **Owner**: All agents coordinated by Rahil
   - **Deliverable**: All 4 final deliverables

### Milestone M2: Proposal Content Complete (End of Week 3)
**Success Criteria**: All 14 content files (7 MD + 7 DOCX) created and validated

### Milestone M3: Visuals & Interactive Complete (End of Week 3)
**Success Criteria**: 21 visual assets + 5 interactive elements completed

### Milestone M4: Proposal Delivered to SAP (End of Week 4)
**Success Criteria**:
- PowerPoint, PDF, Technical Appendix, HTML viewer all complete
- Quality validation passed (BCG/McKinsey 9.5/10 standard)
- GitHub repository initialized with benchmarking codebase
- Ready for stakeholder outreach

**Validation**:
- Internal team review (each member reviews all deliverables)
- BCG/McKinsey quality checklist passed
- All citations verified
- Design system compliance verified

---

## Phase 2: Infrastructure & Dataset Preparation (Weeks 4-5)

**Duration**: December 1 - December 13, 2025 (2 weeks, overlaps with Week 4)

**Objective**: Set up complete infrastructure for benchmarking experiments and prepare all 71 datasets.

### Week 4-5 Tasks

**Infrastructure Setup**:
1. **UW Tillicum Access**
   - Apply for demo account
   - Secure research allocation for H200 GPUs
   - Test connectivity and job submission
   - **Owner**: Mathew
   - **Timeline**: Week 4

2. **Docker Environments**
   - Build `sap-rpt1:v1.0` container (Python 3.11, RPT-1 dependencies)
   - Build `tabpfn:v2.5` container (Python 3.9, TabPFN dependencies)
   - Build `autogluon:v1.0` container (Python 3.8, AutoGluon/MXNet)
   - Build `gradient-boost:v1.0` container (XGBoost, CatBoost, LightGBM)
   - Test all containers with "hello world" experiments
   - **Owner**: Siddarth
   - **Timeline**: Week 4-5

**Dataset Preparation**:
3. **Dataset Download**
   - Download 51 TabArena datasets from TabArena API
   - Download 20 TabZilla datasets from OpenML/Zenodo
   - Verify checksums for data integrity
   - **Owner**: Mathew
   - **Timeline**: Week 5

4. **Dataset Preprocessing**
   - Handle missing values (imputation strategies per model requirements)
   - Encode categorical features (one-hot, label encoding)
   - Generate train/test splits with fixed random seed (42)
   - Create 10-fold cross-validation indices
   - **Owner**: Mathew
   - **Timeline**: Week 5

5. **Data Validation**
   - Cross-reference dataset statistics with published papers
   - Detect anomalies or corrupted data
   - Generate dataset manifest with metadata
   - **Owner**: Shreyas
   - **Timeline**: Week 5

**Code Repository Finalization**:
6. **Model Wrappers**
   - Complete RPT-1 wrapper with ConTextTab default config
   - Complete TabPFN wrapper with Nature paper config
   - Complete TabICL wrapper
   - Complete AutoGluon wrapper (medium_quality preset)
   - Complete XGBoost/CatBoost/LightGBM wrappers with grid search
   - **Owner**: Siddarth
   - **Timeline**: Week 5

7. **Evaluation Pipeline**
   - Implement cross-validation loop
   - Implement metrics calculation (ROC-AUC, Accuracy, F1, R², time)
   - Implement logging and result storage (CSV)
   - Implement error handling (timeout, OOM, exceptions)
   - **Owner**: Siddarth
   - **Timeline**: Week 5

### Milestone M5: Infrastructure & Datasets Ready (End of Week 5)

**Success Criteria**:
- UW Tillicum GPU access secured
- All 4 Docker containers built and tested
- All 71 datasets downloaded, validated, and preprocessed
- Complete benchmarking codebase functional (end-to-end test on 1 dataset)
- Dataset manifest and documentation complete

**Validation**:
- Run end-to-end test: 1 model × 1 dataset → verify results match expected format
- Checksum validation for all datasets
- Docker container smoke tests

---

## Phase 3: Benchmarking Experiments (Weeks 6-10)

**Duration**: December 14, 2025 - January 17, 2026 (5 weeks)

**Objective**: Execute all 497 experiments (7 models × 71 datasets) with 10-fold cross-validation.

### Week 6: Baseline Models

**Tasks**:
1. Run XGBoost on all 71 datasets (10-fold CV)
2. Run CatBoost on all 71 datasets (10-fold CV)
3. Run LightGBM on all 71 datasets (10-fold CV)
   - **Owner**: Siddarth (execution), Shreyas (monitoring)
   - **Estimated GPU Hours**: 15 hours
   - **Cost**: $13.50

**Validation**:
- Cross-reference XGBoost results with published benchmarks (TabArena baselines)
- Identify any anomalous results or implementation bugs
- Verify metrics calculation correctness

### Week 7: SAP RPT-1 Experiments

**Tasks**:
1. Run SAP RPT-1-OSS on all 71 datasets (10-fold CV)
2. Monitor for failures (timeout, OOM, exceptions)
3. Handle edge cases (datasets exceeding RPT-1 limits)
   - **Owner**: Siddarth (execution), Mathew (infrastructure monitoring)
   - **Estimated GPU Hours**: 30 hours
   - **Cost**: $27.00

**Critical Path Item**: RPT-1 is primary model of interest; prioritize debugging any issues.

### Week 8: TabPFN & TabICL Experiments

**Tasks**:
1. Run TabPFN v2.5 on compatible datasets (≤10K rows, ≤500 features)
   - Subsample larger datasets to TabPFN-compatible size
   - Document subsample strategy in appendix
2. Run TabICL on all 71 datasets (10-fold CV)
   - **Owner**: Siddarth
   - **Estimated GPU Hours**: 35 hours (15 TabPFN + 20 TabICL)
   - **Cost**: $31.50

### Week 9: AutoGluon Experiments

**Tasks**:
1. Run AutoGluon Tabular (medium_quality preset) on all 71 datasets
   - Set 1-hour time limit per fold
   - Monitor for memory issues on large datasets
   - **Owner**: Siddarth
   - **Estimated GPU Hours**: 25 hours
   - **Cost**: $22.50

### Week 10: Supplementary Experiments & Re-Runs

**Tasks**:
1. Re-run failed experiments (timeout, OOM, bugs)
2. Run lightweight configurations (efficiency analysis)
3. Run full configurations (maximum accuracy analysis)
4. Verify reproducibility (re-run subset with different random seed)
   - **Owner**: Siddarth
   - **Estimated GPU Hours**: 15 hours
   - **Cost**: $13.50

**Buffer**: Week 10 provides cushion for unexpected delays or debugging.

### Milestone M6: All Benchmarking Experiments Complete (End of Week 10)

**Success Criteria**:
- 497 experiments (7 models × 71 datasets) completed
- Results stored in structured CSV format
- <5% failure rate (handle timeouts/OOM gracefully)
- Total GPU hours ≤120 hours (within moderate budget)
- Raw results backed up to cloud storage

**Validation**:
- Verify all expected result files exist
- Check for missing data or corrupted results
- Sanity check: baseline model performance matches published benchmarks

---

## Phase 4: Statistical Analysis (Week 11)

**Duration**: January 18 - January 24, 2026 (1 week)

**Objective**: Perform rigorous statistical testing and generate publication-quality visualizations.

### Week 11 Tasks

**Statistical Testing**:
1. **Friedman Test**
   - Aggregate cross-validation results (mean per model-dataset pair)
   - Apply Friedman test for overall significance
   - Report test statistic, p-value, degrees of freedom
   - **Owner**: Shreyas

2. **Nemenyi Post-Hoc Analysis**
   - Pairwise comparison between all 7 models
   - Calculate critical difference (CD) value
   - Identify statistically significant differences
   - **Owner**: Shreyas

3. **Critical Difference Diagram**
   - Generate CD diagram visualizing model rankings
   - Annotate with statistical significance
   - **Owner**: Shreyas

4. **Wilcoxon Signed-Rank Tests**
   - Direct pairwise comparison: RPT-1 vs each competitor
   - Apply Bonferroni correction (α = 0.05 / 6 = 0.0083)
   - Calculate effect sizes (Cohen's d)
   - **Owner**: Shreyas

**Subgroup Analyses**:
5. Performance by dataset size (<1K, 1K-10K, 10K-100K, >100K rows)
6. Performance by domain (finance, healthcare, retail, etc.)
7. Performance by feature types (numerical, categorical, mixed)
8. Accuracy-vs-efficiency trade-off analysis
   - **Owner**: Shreyas

**Visualization**:
9. Generate all publication figures:
   - Performance heatmap (7 models × 71 datasets)
   - Box plots by model
   - Scatter plots (accuracy vs training time, accuracy vs inference time)
   - Subgroup comparison charts
   - **Owner**: Shreyas (with Siddarth for scripting)

### Milestone M7: Statistical Analysis Complete (End of Week 11)

**Success Criteria**:
- Friedman test and Nemenyi analysis complete with p-values
- Critical difference diagram generated
- All publication-quality figures created
- Subgroup analyses documented
- Statistical findings summarized for paper

**Validation**:
- Verify statistical test implementation against reference implementations (scipy.stats)
- Peer review of interpretation (check for Type I/II errors)
- Ensure visualizations meet NeurIPS/ICML figure guidelines

---

## Phase 5: Paper Writing (Week 12)

**Duration**: January 25 - January 31, 2026 (1 week)

**Objective**: Draft NeurIPS/ICML conference paper and finalize all deliverables.

### Week 12 Tasks

**Paper Drafting** (NeurIPS/ICML format, 8-10 pages):

1. **Introduction** (1.5 pages)
   - Motivation for tabular foundation model benchmarking
   - Research gap: lack of independent RPT-1 evaluation
   - Contributions: first comprehensive benchmark, statistical rigor, reproducibility
   - **Owner**: Rahil

2. **Related Work** (1 page)
   - Tabular foundation models (TabPFN, TabICL, RPT-1)
   - AutoML platforms (AutoGluon, H2O.ai)
   - Prior benchmarking studies (TabArena, TabZilla)
   - **Owner**: Siddarth

3. **Methodology** (2 pages)
   - Three-pillar approach overview
   - Models, datasets, evaluation metrics
   - Statistical testing protocol
   - Reproducibility measures
   - **Owner**: Rahil + Siddarth

4. **Results** (2.5 pages)
   - Overall performance comparison (Friedman test, Nemenyi)
   - Critical difference diagram
   - Subgroup analyses (by dataset size, domain)
   - Accuracy-efficiency trade-offs
   - **Owner**: Shreyas

5. **Discussion** (1.5 pages)
   - When does RPT-1 excel? When does it underperform?
   - Implications for enterprise adoption
   - Optimization opportunities for SAP
   - Limitations and future work
   - **Owner**: Rahil

6. **Conclusion** (0.5 pages)
   - Summary of findings
   - Call to action for tabular AI community
   - **Owner**: Rahil

**Technical Appendix** (30-40 pages):
7. Per-dataset results tables
8. Detailed statistical test outputs
9. Model hyperparameter configurations
10. Dataset preprocessing details
11. Failure mode analysis (timeouts, OOM)
    - **Owner**: Shreyas + Mathew

**Final Deliverables**:
12. Finalize PowerPoint presentation (update with actual results)
13. Finalize PDF report (update with actual results)
14. Update interactive HTML viewer with real data
15. Finalize GitHub repository (README, documentation, reproducibility guide)
    - **Owner**: All team members

### Milestone M8: Paper Draft Complete (End of Week 12)

**Success Criteria**:
- NeurIPS/ICML paper draft complete (8-10 pages)
- Technical appendix complete (30-40 pages)
- All deliverables updated with actual experimental results
- GitHub repository polished and documented
- Ready for SAP review and conference submission

**Validation**:
- Internal peer review (each member reads paper critically)
- LaTeX compilation passes
- All figures referenced correctly
- Citations complete and formatted (APA/ACM style)
- Reproducibility checklist complete

---

## Stakeholder Engagement Timeline

**Parallel to Execution Phases**:

### Week 3: Initial Outreach (Tier 1)
- Email Walter Sun (Global Head of AI, SAP) via UW faculty introduction
- Share 1-page research proposal and value proposition
- Request informational meeting
- **Owner**: Rahil

### Week 4: Tier 1 Follow-Up + Tier 2 Expansion
- Follow up with Walter Sun
- Reach out to Sam Thelin (ConTextTab lead author)
- Reach out to Johannes Hoffart (Research Director)
- Share full proposal deliverables (PowerPoint, PDF)
- **Owner**: Rahil

### Week 5: Technical Collaboration Initiation
- Schedule call with Sam Thelin to discuss RPT-1 configuration
- Request feedback on methodology
- Explore co-authorship potential
- **Owner**: Rahil + Siddarth

### Week 7: Mid-Project Check-In
- Share progress update with SAP stakeholders
- Report preliminary baseline results
- Address any methodology concerns
- **Owner**: Rahil

### Week 10: Results Preview
- Share preliminary findings with SAP team
- Present early statistical analysis
- Discuss publication co-authorship
- **Owner**: Rahil + Shreyas

### Week 12: Final Presentation
- Present complete results to SAP leadership
- Discuss NeurIPS/ICML submission plan
- Explore ongoing collaboration opportunities
- **Owner**: All team members

---

## Risk Mitigation & Contingency Plans

**Risk**: UW Tillicum GPU unavailable
- **Mitigation**: Apply for access in Week 4; secure AWS/Azure backup credits
- **Contingency**: Pivot to AWS p3.2xlarge ($3.06/hour); increases budget to $367

**Risk**: Dataset download failures
- **Mitigation**: Implement retry logic; verify checksums
- **Contingency**: TabArena/TabZilla hosted on stable infrastructure; low probability

**Risk**: Experiment runtime overruns (>120 GPU hours)
- **Mitigation**: Set 4-hour timeout per model-dataset; monitor progress daily
- **Contingency**: Request budget increase to $180 (conservative scenario)

**Risk**: Statistical significance not achieved
- **Mitigation**: 71 datasets provide high statistical power
- **Contingency**: Report as "RPT-1 competitive but not superior"; still valuable finding

**Risk**: SAP stakeholder non-response
- **Mitigation**: Multi-channel outreach (email, LinkedIn, UW faculty introduction)
- **Contingency**: Proceed with independent benchmarking; publication still valuable

**Risk**: Team member unavailability
- **Mitigation**: Cross-training on critical tasks; documentation
- **Contingency**: Redistribute workload among remaining 3 members

---

## Success Metrics

**Academic Impact**:
- ✅ NeurIPS/ICML 2026 submission ready by Week 12
- ✅ Open-source codebase with 100+ GitHub stars within 6 months
- ✅ Cited by 5+ follow-on papers within 12 months

**SAP Value**:
- ✅ Actionable recommendations incorporated into SAP AI Foundation roadmap
- ✅ Use case guidance adopted by SAP account teams
- ✅ Co-authorship opportunity with SAP researchers

**Team Learning**:
- ✅ Publication-quality research experience for all 4 members
- ✅ SAP collaboration strengthening career prospects
- ✅ Tabular AI expertise attractive to employers

---

## Conclusion

This 12-week timeline balances **rigor** (5 weeks of experiments, 1 week of statistical analysis, 1 week of writing) with **agility** (2-week proposal sprint, iterative stakeholder engagement). Parallel execution in Weeks 3-5 (content, visuals, infrastructure) maximizes efficiency. Built-in buffer in Week 10 mitigates experiment delays. Clear milestones and ownership ensure accountability.

**Critical Path**: Weeks 6-10 (benchmarking experiments) are bottleneck; success depends on robust infrastructure setup in Weeks 4-5.

**Next Step**: Complete Phase 1 (proposal development) by Week 4 to initiate SAP stakeholder engagement.

---

**Document Version**: 1.0
**Last Updated**: November 8, 2025
**Classification**: Proposal - Timeline & Milestones
**Source**: Project requirements analysis and shared-data.json
