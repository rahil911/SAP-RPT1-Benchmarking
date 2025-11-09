# SAP RPT-1 Benchmarking Study
## Problem Statement

**Framework**: SCR (Situation-Complication-Resolution)

**Target Audience**: SAP AI Foundation leadership, academic researchers, enterprise decision-makers

---

## SITUATION: The Emergence of Tabular Foundation Models

### The Tabular AI Landscape

Tabular data represents **80-90% of enterprise data** across industries (Hollmann et al., 2025), powering critical business decisions in finance, healthcare, retail, and manufacturing. For decades, gradient boosting methods (XGBoost, CatBoost, LightGBM) have dominated tabular machine learning, requiring dataset-specific hyperparameter tuning and lacking generalization capabilities across tasks.

The emergence of **foundation models** in natural language processing (GPT-4) and computer vision (CLIP) demonstrated the power of pre-trained models that generalize across diverse tasks without task-specific fine-tuning. This paradigm shift raised a compelling question: **Can foundation models transform tabular AI?**

### SAP RPT-1: A Breakthrough Innovation

In November 2025, SAP AI Foundation released **RPT-1 (ConTextTab)**, marketed as the **first enterprise relational foundation model for tabular data** (Spinaci et al., 2025). Unlike traditional tabular ML models that treat features as independent variables, RPT-1 employs:

1. **Relational Architecture**: Understands semantic relationships between columns and tables
2. **In-Context Learning**: Adapts to new tasks using few-shot examples without fine-tuning
3. **Zero-Shot Prediction**: Generates predictions on unseen datasets with minimal configuration
4. **Semantic Awareness**: Leverages column names and metadata to improve understanding

**Performance Claims** (from ConTextTab paper):
- Competitive performance against AutoGluon on TabArena subset
- Superior performance on datasets with rich semantic structure
- Faster deployment compared to traditional AutoML (no hyperparameter search required)
- Scalable architecture supporting datasets up to 100K rows

**Open-Source Release**: SAP released `sap-rpt-1-oss` on GitHub (November 2025) with 172M parameters (16M trainable), democratizing access to enterprise-grade tabular foundation models.

### Market Context & Strategic Importance

The global **tabular AI market** is estimated at **$8.5B in 2025, growing at 24% CAGR** through 2030 (Gartner, 2025). Key market dynamics:

- **Enterprise Adoption**: 78% of enterprises use tabular ML for business-critical applications (McKinsey, 2024)
- **AutoML Growth**: AutoML platforms (AutoGluon, H2O.ai, DataRobot) reached $1.2B market size in 2024
- **Foundation Model Momentum**: Following TabPFN's Nature publication (2025), foundation models gained credibility in tabular AI
- **Vendor Competition**: Microsoft (TabICL), PriorLabs (TabPFN), and AutoGluon compete for tabular AI leadership

**SAP's Strategic Stakes**:
- Position RPT-1 as differentiated enterprise solution versus open-source competitors
- Validate R&D investment in SAP AI Foundation (estimated $50M+ annually)
- Enable SAP Business AI suite integration (S/4HANA, SuccessFactors, Ariba)
- Attract academic talent through credible research contributions

---

## COMPLICATION: The Validation Gap

### No Independent, Comprehensive Benchmarking Exists

Despite SAP's bold claims, **critical validation gaps** undermine RPT-1's credibility:

#### 1. Limited Third-Party Evaluation

**Problem**: The ConTextTab paper (Spinaci et al., 2025) presents RPT-1 results on a **TabArena subset** (estimated 15-20 datasets), but:
- No comprehensive comparison across 70+ TabArena datasets
- No evaluation against TabPFN v2.5 (published in Nature 2025 after RPT-1 development)
- No rigorous statistical testing (Friedman, Nemenyi) to establish significance
- No independent replication by external researchers

**Impact**: Enterprise decision-makers lack confidence in performance claims without third-party validation.

#### 2. Unclear Competitive Positioning

**Problem**: The tabular AI landscape evolved rapidly in 2024-2025:
- **TabPFN v2.5** (Nature 2025): State-of-the-art transformer-based foundation model
- **TabICL** (ICML 2025): Scalable in-context learning approach from Microsoft Research
- **AutoGluon 1.0**: Production-grade AutoML with ensemble methods

**Current State**: No head-to-head comparison exists answering:
- When does RPT-1 outperform TabPFN? When does it underperform?
- How does RPT-1's in-context learning compare to TabICL?
- What are the accuracy-vs-efficiency trade-offs versus AutoGluon?
- Do traditional gradient boosting methods still dominate on large datasets?

**Impact**: SAP cannot provide evidence-based guidance on when enterprises should deploy RPT-1 versus alternatives, limiting adoption.

#### 3. Unquantified Use Case Scenarios

**Problem**: The ConTextTab paper lacks **prescriptive guidance** for practitioners:
- Which dataset characteristics favor RPT-1? (dataset size, feature types, semantic richness)
- What is the computational cost versus accuracy trade-off?
- How does performance scale with dataset size (1K vs 10K vs 100K rows)?
- When should enterprises choose RPT-1 over XGBoost?

**Impact**: Without clear decision frameworks, enterprises default to proven solutions (XGBoost, AutoGluon), delaying RPT-1 adoption.

#### 4. Academic Credibility Gap

**Problem**: SAP RPT-1 lacks **peer-reviewed validation** from independent academic institutions:
- ConTextTab paper authored exclusively by SAP researchers (potential bias perception)
- No replication studies by universities or research labs
- Limited citations in academic literature (too recent for impact)
- Absent from major ML benchmarking suites (Papers With Code, OpenML)

**Impact**: Academic community cannot assess RPT-1's scientific contribution without rigorous third-party evaluation, limiting citation potential and research community engagement.

#### 5. Reproducibility Concerns

**Problem**: While SAP released `sap-rpt-1-oss` on GitHub, **reproducibility gaps** persist:
- No standardized benchmarking codebase comparing RPT-1 to competitors
- Inconsistent evaluation protocols across different papers (TabPFN, AutoGluon, RPT-1)
- Lack of frozen computational environments (Docker) ensuring exact replication
- No public dataset splits or random seeds for fair comparison

**Impact**: Researchers cannot reliably reproduce or extend RPT-1 evaluations, hindering scientific progress.

### Quantified Business Impact

The validation gap creates measurable business consequences for SAP:

1. **Delayed Enterprise Adoption**: Estimated **$25M+ revenue at risk** in Year 1 due to buyer hesitation without third-party validation
2. **Competitive Disadvantage**: AutoGluon and TabPFN have academic credibility (Nature publications, university partnerships) that RPT-1 lacks
3. **R&D Uncertainty**: SAP AI Foundation cannot prioritize optimization efforts without knowing where RPT-1 underperforms
4. **Talent Acquisition**: Limited academic engagement reduces SAP's appeal to top-tier ML researchers
5. **Partnership Barriers**: Potential SAP Business AI integrations delayed pending performance evidence

### Why Current Approaches Fail

**Existing solutions are insufficient**:

1. **Vendor Benchmarks**: SAP's internal evaluation lacks independent credibility
2. **Crowdsourced Leaderboards**: TabArena provides infrastructure but no comprehensive RPT-1 evaluation exists
3. **Ad-Hoc Comparisons**: Individual researchers may test RPT-1 on 1-2 datasets, but not systematically across diverse domains
4. **Industry Analysts**: Gartner/Forrester lack technical depth for rigorous ML benchmarking

**What's Missing**: A **publication-quality, independent academic benchmarking study** conducted by a credible research institution with expertise in tabular AI, statistical rigor, and no commercial conflicts of interest.

---

## RESOLUTION: UW MSIM Benchmarking Study

### Our Proposed Solution

The University of Washington Master of Science in Information Management (UW MSIM) team proposes a **12-week comprehensive benchmarking study** that addresses all identified validation gaps through rigorous academic methodology.

### Solution Design

**Objective**: Conduct the **first independent, comprehensive, publication-quality benchmarking** of SAP RPT-1 against state-of-the-art tabular AI models, suitable for NeurIPS 2026 or ICML 2026 submission.

**Scope**:
- **71 datasets** from TabArena and TabZilla benchmarks (classification and regression)
- **7 models**: SAP RPT-1-OSS, TabPFN v2.5, TabICL, AutoGluon, XGBoost, CatBoost, LightGBM
- **5 evaluation metrics**: ROC-AUC, Accuracy, F1-score, Training Time, Inference Time
- **Statistical rigor**: Friedman test, Nemenyi post-hoc, critical difference diagrams
- **Reproducibility**: Docker environments, public GitHub repository, REFORMS checklist

### Three-Pillar Methodology

**Pillar 1: Comprehensive Model Coverage**
- Evaluate RPT-1 against **complete competitive landscape** (foundation models, AutoML, traditional ML)
- Test multiple model configurations (lightweight, standard, full) to assess accuracy-efficiency trade-offs
- Include baseline models (XGBoost, CatBoost) to ground performance claims

**Pillar 2: Statistical Rigor**
- Apply **Friedman test** for overall statistical significance across models
- Use **Nemenyi post-hoc analysis** for pairwise model comparisons
- Generate **critical difference diagrams** visualizing performance rankings
- Employ **10-fold cross-validation** to reduce variance in estimates

**Pillar 3: Reproducibility & Transparency**
- Provide **Docker-based frozen environments** ensuring exact replication
- Publish **complete codebase** on GitHub with dataset download scripts
- Document **compute costs and runtime** for transparency
- Follow **REFORMS checklist** (Reporting Standards for ML-based Science)

### Differentiation from Existing Work

**Versus ConTextTab Paper**:
- **71 datasets** (vs ~15-20 in original paper)
- **Independent evaluation** (no SAP authorship bias)
- **Head-to-head comparison** with TabPFN v2.5 (not available when ConTextTab written)
- **Statistical significance testing** (Friedman/Nemenyi)

**Versus Ad-Hoc Evaluations**:
- **Systematic coverage** across diverse domains (finance, healthcare, retail, etc.)
- **Standardized protocols** ensuring fair comparison
- **Publication-quality** rigor suitable for NeurIPS/ICML

**Versus Vendor Benchmarks**:
- **Academic independence** (no commercial incentives)
- **Open-source reproducibility** (no proprietary data or code)
- **Peer review** through conference submission

### Expected Deliverables

**For SAP**:
1. **Validation Report** (25-35 pages): Comprehensive performance assessment with executive recommendations
2. **Technical Appendix** (30-40 pages): Detailed experimental results, statistical analysis, methodology
3. **Use Case Guidance**: Decision framework for when to deploy RPT-1 vs alternatives
4. **Competitive Intelligence**: Quantified positioning versus TabPFN, AutoGluon, traditional ML
5. **Optimization Roadmap**: Performance gap analysis identifying improvement opportunities

**For Academic Community**:
1. **NeurIPS/ICML Paper** (8-10 pages): Publication-quality benchmarking study
2. **Open-Source Codebase**: GitHub repository enabling reproducibility and extension
3. **Benchmark Dataset Suite**: Standardized evaluation framework for future tabular foundation models

**For Enterprise Decision-Makers**:
1. **Adoption Framework**: Clear guidance on RPT-1 deployment scenarios
2. **ROI Analysis**: Cost-benefit assessment including computational efficiency
3. **Risk Assessment**: Transparent evaluation of limitations and failure modes

### Value Proposition for SAP

**Immediate Benefits**:
- **Independent Validation**: Credible third-party assessment strengthening enterprise sales conversations (comparable to $50K+ consulting engagement)
- **Competitive Positioning**: Data-driven comparison clarifying advantages versus TabPFN, AutoGluon, and XGBoost
- **Use Case Clarity**: Prescriptive guidance enabling SAP account teams to recommend RPT-1 confidently
- **Academic Credibility**: UW partnership and potential NeurIPS/ICML publication raising RPT-1's research profile

**Long-Term Benefits**:
- **Product Roadmap**: Performance analysis identifying optimization priorities for SAP AI Foundation
- **Talent Pipeline**: Engagement with UW MSIM students as potential recruiting targets
- **Research Collaboration**: Foundation for ongoing UW-SAP partnership on tabular AI research
- **Citation Impact**: Academic publication driving organic interest from ML research community

**UW Connection Advantage**: SAP Global Head of AI **Walter Sun** holds UW affiliate faculty status, providing direct engagement pathway and institutional credibility.

### Why Our Team?

The UW MSIM team brings **unique qualifications** for this benchmarking study:

1. **Academic Independence**: No commercial conflicts of interest ensuring unbiased evaluation
2. **Technical Expertise**: 14+ combined years across AI/ML, cloud infrastructure, and data engineering (AWS, SAP, Morgan Stanley backgrounds)
3. **SAP Domain Knowledge**: Team member with direct SAP India experience and 100+ SAP CPI integrations deployed
4. **Publication Track Record**: IEEE Best Paper Award 2023, experience with conference submissions
5. **Entrepreneurial Perspective**: Co-founders with proven ability to deliver production-quality systems under deadlines

### Research Questions Addressed

Our benchmarking study will rigorously answer:

**RQ1**: How does SAP RPT-1 performance compare to TabPFN v2.5 and TabICL across diverse tabular datasets?

**RQ2**: Under what conditions (dataset size, feature types, semantic richness) does RPT-1 outperform traditional gradient boosting and AutoML?

**RQ3**: What are the accuracy-vs-computational-efficiency trade-offs between RPT-1 and competing approaches?

**RQ4**: How does RPT-1's in-context learning capability generalize across domains (finance, healthcare, retail, etc.)?

**RQ5**: What optimization opportunities exist to improve RPT-1 performance on currently underperforming dataset types?

### Success Metrics

We define success as:

**Academic Impact**:
- NeurIPS 2026 or ICML 2026 acceptance (acceptance rate: ~25%)
- Open-source codebase with 100+ GitHub stars within 6 months
- Cited by 5+ follow-on papers within 12 months

**SAP Value**:
- Actionable recommendations incorporated into SAP AI Foundation roadmap
- Use case guidance adopted by SAP account teams for RPT-1 positioning
- Co-authorship opportunity with SAP researchers (Sam Thelin, Johannes Hoffart)

**Enterprise Impact**:
- Decision framework adopted by 3+ enterprises evaluating RPT-1
- Reproducible benchmarking methodology used for future tabular foundation model evaluations

---

## Conclusion

SAP RPT-1 represents a promising innovation in tabular AI, but **validation gaps** currently limit enterprise adoption and academic credibility. Our UW MSIM team proposes a **rigorous, independent benchmarking study** that fills this gap through comprehensive model coverage, statistical rigor, and reproducible methodology.

This 12-week project delivers **immediate value** to SAP (independent validation, competitive intelligence, use case guidance) while contributing **lasting impact** to the academic community (publication-quality research, open-source tools, benchmark standardization).

**Next Steps**: Initiate collaboration with SAP AI Foundation stakeholders (Walter Sun, Sam Thelin, Johannes Hoffart) to align methodology and ensure mutual benefit.

---

**Document Version**: 1.0
**Last Updated**: November 8, 2025
**Classification**: Proposal - Problem Statement (SCR Framework)

**References**:
- Spinaci, M., Polewczyk, M., Schambach, M., & Thelin, S. (2025). ConTextTab: A Semantics-Aware Tabular In-Context Learner. NeurIPS 2025. arXiv:2506.10707
- Hollmann, N., Müller, S., & Hutter, F. (2025). Accurate predictions on small data with a tabular foundation model. Nature. https://doi.org/10.1038/s41586-024-08328-6
- AutoGluon Team. (2025). TabArena: A Living Benchmark for Tabular Prediction. arXiv:2506.16791
- Gartner. (2025). Market Analysis: Enterprise AI Platforms, 2025. Gartner Research.
- McKinsey. (2024). The State of AI in 2024: Enterprise Adoption Trends. McKinsey Digital.
