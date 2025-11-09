# SAP RPT-1 Benchmarking Study
## Executive Summary

**Project Title**: Independent Academic Benchmarking of SAP RPT-1 Against State-of-the-Art Tabular AI Models

**Institution**: University of Washington, Master of Science in Information Management

**Timeline**: 12 weeks (November 8, 2025 - January 31, 2026)

**Target Publication**: NeurIPS 2026 / ICML 2026

---

## Problem Statement

SAP RPT-1 (ConTextTab) represents a groundbreaking innovation as the first enterprise relational foundation model for tabular data, launched in November 2025. The model promises semantic-aware in-context learning and zero-shot prediction capabilities that could transform how enterprises approach tabular AI. However, **no independent, comprehensive academic benchmarking currently exists** to validate SAP's performance claims or clarify when RPT-1 excels versus traditional machine learning approaches.

This validation gap creates significant uncertainty for enterprise decision-makers evaluating RPT-1 adoption and limits SAP's ability to provide evidence-based positioning guidance. The academic community also lacks rigorous third-party evaluation necessary to assess RPT-1's contribution to the tabular AI landscape.

---

## Solution Approach

Our team proposes a **publication-quality benchmarking study** that evaluates SAP RPT-1 against 6+ competing tabular AI models across 70+ real-world datasets. This comprehensive assessment will employ rigorous statistical testing (Friedman test, Nemenyi post-hoc analysis) and adhere to NeurIPS/ICML publication standards for reproducibility.

**Three-Pillar Methodology**:

1. **Comprehensive Model Coverage**: Benchmark 7 models including SAP RPT-1-OSS, TabPFN v2.5, TabICL, AutoGluon, XGBoost, CatBoost, and LightGBM
2. **Statistical Rigor**: 10-fold cross-validation with statistical significance testing across multiple performance metrics (ROC-AUC, accuracy, F1-score, training time, inference time)
3. **Reproducibility**: Docker-based frozen environments, public GitHub repository with complete codebase, and REFORMS checklist compliance

The study will leverage 71 datasets from TabArena and TabZilla benchmarks, covering diverse domains including finance, healthcare, retail, manufacturing, government, education, and technology.

---

## Team Qualifications

Our team brings **14+ combined years of experience** across Fortune 500 companies and startups, with deep expertise in AI/ML, cloud infrastructure, data engineering, and product management.

**Team Composition** (Match Scores from Project Requirements Analysis):

- **Rahil M. Harihar** (94% match) - Product Lead & AI/ML Strategy
  - Former SAP India consultant with 100+ SAP CPI integrations deployed
  - Founded bootstrapped startup with $36K profit and 90% ML model accuracy
  - Expertise: Product management, multi-agent systems, enterprise integration

- **Siddarth Bhave** (92% match) - Technical Lead & AI/ML Infrastructure
  - AWS (DynamoDB) and Morgan Stanley engineering background
  - Achieved $1M annual cost savings through infrastructure optimization
  - Expertise: LLMs, RAG, prompt engineering, backend systems, Docker/Kubernetes

- **Mathew Jerry Meleth** (88% match) - Data Engineering & Cloud Infrastructure
  - Rocket Mortgage, Mu Sigma, and Adobe experience
  - Reduced processing time from 1 month to 2 days (93% improvement)
  - Expertise: AWS, Azure, PySpark, Hadoop, ETL/ELT pipelines

- **Shreyas B Subramanya** (86% match) - Operations & Analytics
  - o9 Solutions supply chain product management
  - Trained 500+ individuals through certification content creation
  - Expertise: Power BI, Tableau, Delta Lake, process optimization

**Team Distinction**: Average GPA 3.86/4.0 | Co-founders with proven startup success | Combined Fortune 500 and entrepreneurial experience

---

## Expected Outcomes

### For SAP

1. **Independent Validation**: First external academic assessment providing credible third-party validation of RPT-1 performance claims
2. **Competitive Positioning**: Systematic comparison clarifying RPT-1's advantages and limitations versus TabPFN, TabICL, and AutoGluon
3. **Use Case Guidance**: Data-driven recommendations identifying optimal scenarios where RPT-1 excels
4. **Publication Impact**: NeurIPS/ICML citation raises RPT-1's profile in academic machine learning community
5. **Talent Pipeline**: UW MSIM engagement creates potential recruiting opportunity and academic partnership

### For Academic Community

1. **First Comprehensive Benchmark**: Publication-quality assessment filling critical research gap
2. **Reproducible Framework**: Open-source codebase enabling future tabular foundation model evaluations
3. **Statistical Rigor**: Methodologically sound comparison suitable for top-tier conference publication

### For Enterprise Decision-Makers

1. **Adoption Framework**: Clear guidance on when to deploy RPT-1 versus traditional ML approaches
2. **Cost-Benefit Analysis**: Quantified trade-offs between accuracy, computational efficiency, and implementation complexity
3. **Risk Mitigation**: Evidence-based assessment reducing uncertainty in enterprise AI investments

---

## Timeline & Key Milestones

**12-Week Project Phases**:

| Phase | Weeks | Focus | Milestone |
|-------|-------|-------|-----------|
| **Research & Planning** | 1-2 | Intelligence gathering, infrastructure setup | Research foundation complete |
| **Proposal Development** | 3-4 | Content creation, visual design, interactive elements | Proposal delivered to SAP |
| **Infrastructure Prep** | 4-5 | Code repository, Docker environments, dataset downloads | 70+ datasets ready |
| **Benchmarking Experiments** | 6-10 | Run experiments across all models and datasets | All experimental runs complete |
| **Analysis & Writing** | 11-12 | Statistical testing, paper drafting | NeurIPS/ICML draft ready |

**Critical Milestones**:
- **Week 2**: Research foundation complete
- **Week 3**: Proposal content complete
- **Week 4**: Proposal delivered to SAP stakeholders
- **Week 10**: Benchmarking experiments complete (70+ datasets, 7 models)
- **Week 12**: Conference paper draft ready for submission

---

## Compute Resources & Budget

**Primary Resource**: UW Tillicum H200 80GB GPUs ($0.90/hour)

**Budget Scenarios**:

| Scenario | Estimated Hours | Estimated Cost | Risk Level |
|----------|----------------|----------------|------------|
| **Optimistic** | 80 hours | $72 | Low - lightweight model configs, efficient parallelization |
| **Moderate** | 120 hours | $108 | Medium - standard configs, some re-runs |
| **Conservative** | 200 hours | $180 | High - full model configs, extensive cross-validation |

**Recommended**: Moderate scenario ($108) balances thoroughness with cost efficiency.

**Backup Resources**: AWS Research Credits (p3.2xlarge V100) and Azure for Students (NC6s v3 V100) available if UW Tillicum unavailable.

---

## Strategic Value for SAP

This benchmarking study delivers **consulting-grade validation** (comparable to $50K+ external research engagement) while creating opportunities for:

- **Academic Credibility**: Independent UW validation strengthens enterprise sales conversations
- **Competitive Intelligence**: Rigorous comparison against TabPFN and AutoGluon clarifies market positioning
- **Product Roadmap**: Performance analysis identifies optimization opportunities
- **Co-authorship Potential**: Collaboration with SAP AI Foundation researchers on NeurIPS/ICML submission
- **Long-Term Partnership**: Foundation for ongoing UW-SAP research collaboration

**UW Connection Advantage**: SAP Global Head of AI Walter Sun's UW affiliate faculty status provides direct engagement pathway.

---

## Next Steps

1. **Week 3**: Initial outreach to Walter Sun (Global Head of AI, SAP) via UW faculty connection
2. **Week 4**: Technical collaboration initiation with Sam Thelin (ConTextTab lead author)
3. **Week 5**: Methodology validation and RPT-1 configuration guidance from SAP team
4. **Week 10**: Preliminary results preview for SAP stakeholders
5. **Week 12**: Co-authorship discussion for NeurIPS/ICML submission

---

## Contact Information

**Team Lead**: Rahil M. Harihar

**Institution**: University of Washington, Master of Science in Information Management

**Project Duration**: November 8, 2025 - January 31, 2026 (12 weeks)

**Deliverables**:
- Comprehensive benchmarking report (25-35 pages)
- Technical appendix (30-40 pages)
- Conference paper draft (8-10 pages, NeurIPS/ICML format)
- Public GitHub repository with complete codebase
- Interactive results dashboard

---

**Document Version**: 1.0
**Last Updated**: November 8, 2025
**Classification**: Proposal - Executive Summary
