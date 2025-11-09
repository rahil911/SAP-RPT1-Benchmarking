# Research Artifacts - SAP RPT-1 Benchmarking Project

**Phase**: Phase 0 - Research Foundation
**Owner**: Research Agent
**Status**: In Progress
**Purpose**: Comprehensive research foundation for publication-quality benchmarking study

---

## 📁 Directory Contents

This folder contains all research artifacts that form the foundation for the SAP RPT-1 benchmarking project. These files are **READ-ONLY** for all agents except the Research Agent.

### Core Research Files (8 Required)

1. **sap-company-intelligence.md** (Target: 30-40 pages)
   - SAP history and AI strategy
   - SAP AI Foundation platform roadmap
   - SAP RPT-1 product positioning
   - Market position and competitive landscape
   - Client list and use cases
   - Sources: SAP website, press releases, industry reports

2. **sap-rpt-technical-deep-dive.md** (Target: 40-50 pages)
   - ConTextTab/SAP RPT-1 paper analysis
   - GitHub repository (sap-rpt-1-oss) documentation
   - Model architecture details
   - Training methodology (T4 dataset, 2.18M tables)
   - Performance claims with citations
   - Limitations and edge cases
   - API specifications and usage
   - Sources: PDF paper, GitHub, Hugging Face

3. **tabular-ml-landscape.md** (Target: 60-80 pages)
   - TabPFN v2.5 (Nature 2025) deep-dive
   - TabICL (ICML 2025) analysis
   - AutoGluon capabilities and architecture
   - Traditional ML baselines (XGBoost, CatBoost, LightGBM)
   - Kumo AI (graph-based approach) if relevant
   - Competitive comparison matrix
   - Technology trends and evolution
   - Sources: Academic papers, GitHub repos, documentation

4. **benchmarking-methodology.md** (Target: 80-100 pages)
   - TabArena methodology and standards
   - TabZilla benchmarking protocols
   - TALENT toolkit approach
   - Statistical testing requirements (Friedman, Nemenyi)
   - Reproducibility checklists (REFORMS)
   - NeurIPS/ICML publication standards
   - Compute reporting requirements (CVPR 2026)
   - Best practices from literature
   - Sources: Benchmark papers, conference CFPs, guidelines

5. **compute-resources-guide.md** (Target: 40-50 pages)
   - UW Tillicum (H200 GPUs, $0.90/hr)
     - Access process and timeline
     - Demo account (100 free hours)
     - Pricing and capabilities
   - AWS Research Credits
     - Application process and requirements
     - Award amounts ($5K per student)
     - Approval timeline (90-120 days)
   - Azure for Students
     - Setup instructions
     - $100 credits per student
   - UW Research Computing Club (Hyak)
     - Free L40S GPU access
     - Join process
   - Budget cloud providers
     - Thunder Compute, Vast.ai, RunPod
     - Pricing comparison
   - Cost estimates (3 scenarios)
   - Sources: UW IT, cloud provider websites, pricing pages

6. **datasets-benchmarks.md** (Target: 50-60 pages)
   - TabArena 51 datasets
     - Dataset descriptions and statistics
     - Download process
     - Storage requirements
   - TabZilla 36 datasets (focus on 20 hardest)
     - Dataset characteristics
     - Difficulty analysis
   - OpenML-CC18 datasets (subset of 15)
     - Curation criteria
     - API access
   - Custom SAP datasets (if applicable)
   - Download scripts and automation
   - Data quality validation
   - Sources: TabArena, TabZilla, OpenML, papers

7. **team-matching.md** (Target: 20-30 pages)
   - Knowledge Graph API query results
   - Team member profiles (RAG-powered)
   - Match scores calculation
     - Rahil M. Harihar: 94% (AI/ML + Product)
     - Siddarth Bhave: 92% (AI/ML Engineering + Infrastructure)
     - Mathew Jerry Meleth: 88% (Cloud + Data)
     - Shreyas B Subramanya: 86% (Analytics + Operations)
   - Role assignments and justifications
   - Skills matrix (18 requirements × 4 members)
   - Individual strengths for this project
   - Sources: Knowledge Graph API, team analysis

8. **kg-data-cache.json** (Generated)
   - Complete team data from Knowledge Graph API
   - Cached for fallback if API fails
   - Schema validation
   - Timestamp and version info

---

## 🎯 Research Agent Tasks

### Priority 1: Immediate (Week 1)

**Task 1.1: SAP Company Intelligence**
- Web research on SAP (20+ sources)
- AI Foundation platform deep-dive
- RPT-1 product launch analysis
- Deliverable: sap-company-intelligence.md

**Task 1.2: Knowledge Graph API Query**
- Query team profiles
- Extract and structure data
- Cache results
- Deliverables: team-matching.md, kg-data-cache.json

### Priority 2: Technical (Week 1-2)

**Task 2.1: SAP RPT-1 Technical Analysis**
- Analyze ConTextTab PDF (already downloaded: 2506.10707v4.pdf)
- Clone and document sap-rpt-1-oss GitHub repo
- Extract model specs, training data, performance
- Deliverable: sap-rpt-technical-deep-dive.md

**Task 2.2: Competitive Landscape Research**
- Research TabPFN, TabICL, AutoGluon
- Clone GitHub repositories
- Document capabilities and limitations
- Create comparison matrix
- Deliverable: tabular-ml-landscape.md

### Priority 3: Methodology (Week 2)

**Task 3.1: Benchmarking Standards**
- Research TabArena, TabZilla, TALENT
- Document statistical protocols
- Extract reproducibility requirements
- Review NeurIPS/ICML CFPs
- Deliverable: benchmarking-methodology.md

**Task 3.2: Compute Resources Analysis**
- UW Tillicum research and documentation
- Cloud credits application guides
- Cost estimation (3 scenarios)
- Deliverable: compute-resources-guide.md

### Priority 4: Datasets (Week 2)

**Task 4.1: Dataset Catalog**
- TabArena 51 datasets documentation
- TabZilla subset selection
- OpenML-CC18 subset identification
- Download scripts creation
- Deliverable: datasets-benchmarks.md

---

## 📊 Research Quality Standards

### Citation Requirements
- **Every claim must have a source**
- APA format for all citations
- URLs with access dates
- Paper citations with arXiv/DOI
- GitHub repos with commit SHAs

### Quantification Standards
- All statistics with numbers (not "significant" but "35% reduction")
- Market sizing with sources ($X billion, CAGR %)
- Performance metrics with exact values
- Timeline estimates with ranges

### Validation Checklist
- [ ] All research files created (8 files)
- [ ] All claims cited with sources
- [ ] All statistics quantified
- [ ] Knowledge Graph API queried
- [ ] Team data cached and validated
- [ ] No fabricated or hallucinated data
- [ ] Cross-references valid
- [ ] File naming follows convention
- [ ] Total research pages: 320-400 (target met)

---

## 🔗 Dependencies

### External APIs
- **Knowledge Graph API**: https://kg-student-backend.ambitiouswave-220155c4.eastus2.azurecontainerapps.io
- **OpenML API**: https://www.openml.org
- **Hugging Face**: https://huggingface.co

### GitHub Repositories to Clone
- SAP RPT-1: https://github.com/SAP-samples/sap-rpt-1-oss
- TabPFN: https://github.com/PriorLabs/TabPFN
- TabICL: https://github.com/soda-inria/tabicl
- TabArena: https://github.com/autogluon/tabarena
- TabZilla: https://github.com/naszilla/tabzilla
- TALENT: https://github.com/LAMDA-Tabular/TALENT
- AutoGluon: https://github.com/autogluon/autogluon

### Papers to Download
- ConTextTab (NeurIPS 2025) - ✅ Already have: 2506.10707v4.pdf
- TabPFN (Nature 2025)
- TabICL (ICML 2025)
- TabArena (arXiv 2025)
- TabZilla (NeurIPS 2023)
- TALENT papers
- AutoGluon papers

---

## 🚀 Downstream Usage

### Who Reads These Files?

**Agent 1 (Content Generator)**:
- Reads ALL research files for context
- Uses team-matching.md for team presentation
- Uses kg-data-cache.json for RAG workflow
- Creates shared-data.json based on research

**Agent 2 (Visual Designer)**:
- Reads research files for diagram content
- Uses team data for team structure diagrams
- Uses timeline for Gantt charts

**Agent 3 (Interactive Developer)**:
- Reads team data for web portal
- Uses research highlights for content

**Agent 4 (Infrastructure Engineer)**:
- Reads compute-resources-guide.md for infrastructure setup
- Uses datasets-benchmarks.md for download automation

**Agent 5 (Project Manager)**:
- Reads all research for task breakdown
- Uses timeline and team assignments

---

## 📝 Notes

- **READ-ONLY for all agents except Research Agent**
- Research must be complete BEFORE content generation starts
- Quality over speed - thorough research prevents rework
- All research feeds into shared-data.json (single source of truth)
- Target: 320-400 total pages of research (100x Graphwise rigor)

---

**Status**: ⏳ In Progress
**Target Completion**: End of Week 2
**Next Milestone**: Create shared-data.json and hand off to Agent 1
