# SAP RPT-1 Benchmarking Study
## Methodology & Experimental Design

**Framework**: Three-Pillar Approach (Comprehensive Coverage, Statistical Rigor, Reproducibility)

**Quality Standard**: NeurIPS/ICML publication-grade methodology

---

## Executive Overview

Our benchmarking methodology employs a **three-pillar approach** ensuring comprehensive, statistically rigorous, and reproducible evaluation of SAP RPT-1 against state-of-the-art tabular AI models.

**Pillar 1 - Comprehensive Model Coverage**: Evaluate 7 models spanning foundation models (RPT-1, TabPFN, TabICL), AutoML platforms (AutoGluon), and traditional baselines (XGBoost, CatBoost, LightGBM) across 71 diverse datasets.

**Pillar 2 - Statistical Rigor**: Apply Friedman test and Nemenyi post-hoc analysis with 10-fold cross-validation to establish statistically significant performance differences.

**Pillar 3 - Reproducibility**: Provide Docker-based frozen environments, public GitHub repository, compute cost transparency, and REFORMS checklist compliance.

---

## Pillar 1: Comprehensive Model Coverage

### Models Under Evaluation (7 Total)

#### Foundation Models (3)

**1. SAP RPT-1-OSS (Small)**
- **Category**: Relational foundation model for tabular data
- **Parameters**: 172M total (16M trainable)
- **Architecture**: Transformer-based with relational encoding
- **Key Features**:
  - Semantic-aware in-context learning
  - Zero-shot and few-shot prediction capabilities
  - Column relationship understanding
  - No hyperparameter tuning required
- **Implementation**: `sap-rpt-1-oss` from GitHub (https://github.com/SAP-samples/sap-rpt-1-oss)
- **Python Version**: 3.11
- **Configuration**: Default ConTextTab settings as specified in Spinaci et al. (2025)

**2. TabPFN v2.5**
- **Category**: Prior-fitted network foundation model
- **Architecture**: Transformer-based with synthetic data pre-training
- **Key Features**:
  - Prior-data fitted networks (PFNs)
  - Fast inference (seconds)
  - No hyperparameter search
  - Handles up to 10K rows, 500 features
- **Implementation**: `tabpfn` from PriorLabs GitHub (https://github.com/PriorLabs/tabpfn)
- **Python Version**: 3.9+
- **Publication**: Hollmann et al., Nature 2025
- **Configuration**: Default settings per Nature paper

**3. TabICL**
- **Category**: In-context learning foundation model
- **Architecture**: Scalable transformer for tabular data
- **Key Features**:
  - In-context learning paradigm
  - Scalable to large datasets
  - Few-shot adaptation
- **Implementation**: `tabicl` from Soda-Inria GitHub (https://github.com/soda-inria/tabicl)
- **Python Version**: 3.9+
- **Publication**: ICML 2025
- **Configuration**: Standard in-context learning setup

#### AutoML Platform (1)

**4. AutoGluon Tabular**
- **Category**: Automated machine learning platform
- **Ensemble Methods**: Stacked ensembles of gradient boosting, neural networks, and KNN
- **Key Features**:
  - Automated feature engineering
  - Hyperparameter optimization
  - Multi-layer stacking
  - Production-grade reliability
- **Implementation**: `autogluon.tabular` (https://github.com/autogluon/autogluon)
- **Python Version**: 3.8+
- **Configuration**: `medium_quality` preset (balanced accuracy/time)
- **Rationale**: TabArena baseline, industry-standard AutoML

#### Traditional Baselines (3)

**5. XGBoost**
- **Category**: Gradient boosting decision trees
- **Key Features**: Fast training, regularization, parallel processing
- **Implementation**: `xgboost` library
- **Configuration**: Grid search over learning rate [0.01, 0.1, 0.3], max depth [3, 6, 9], n_estimators [100, 500]
- **Rationale**: Industry baseline for tabular ML

**6. CatBoost**
- **Category**: Gradient boosting with categorical feature handling
- **Key Features**: Robust to categorical features, minimal tuning
- **Implementation**: `catboost` library
- **Configuration**: Default parameters with automatic categorical detection
- **Rationale**: Strong performance on heterogeneous feature types

**7. LightGBM**
- **Category**: Gradient boosting with histogram-based learning
- **Key Features**: Fast training, memory efficient, leaf-wise growth
- **Implementation**: `lightgbm` library
- **Configuration**: Default parameters optimized for speed
- **Rationale**: Efficient baseline for large datasets

### Model Configurations

To assess **accuracy-vs-efficiency trade-offs**, we evaluate each model in multiple configurations:

| Model | Lightweight | Standard | Full |
|-------|-------------|----------|------|
| **RPT-1** | Default config | Default config | Default config |
| **TabPFN** | Default config | Default config | N/A (single config) |
| **TabICL** | Default config | Default config | Default config |
| **AutoGluon** | `best_quality` with 1hr time limit | `medium_quality` | `best_quality` with 4hr time limit |
| **XGBoost** | n_estimators=100 | n_estimators=500 | Grid search |
| **CatBoost** | Default | Default with auto-tuning | Bayesian optimization |
| **LightGBM** | Default | Default | Grid search |

**Primary Analysis**: Standard configuration results
**Supplementary Analysis**: Lightweight (efficiency) and Full (maximum accuracy) configurations

---

## Pillar 2: Statistical Rigor

### Datasets & Benchmark Suites

**Total Datasets**: 71 (classification and regression)

#### TabArena Benchmark (51 datasets)
**Source**: TabArena (https://tabarena.ai) - Living benchmark for tabular prediction
**Characteristics**:
- **Domain Diversity**: Finance, healthcare, retail, government, technology, science
- **Size Range**: 768 rows (diabetes) to 1,025,010 rows (poker-hand)
- **Feature Range**: 8 features (electricity) to 54 features (jannis)
- **Task Types**: Binary classification, multi-class classification, regression
- **Missing Data**: Varied (0% to 30% missing values)

**Representative Datasets**:
- **adult**: Income prediction (48,842 rows, 14 features, binary classification)
- **bank-marketing**: Marketing campaign success (45,211 rows, 16 features, binary)
- **credit-g**: Credit risk assessment (1,000 rows, 20 features, binary)
- **higgs**: Particle physics classification (98,050 rows, 28 features, binary)
- **jannis**: Multi-class classification (83,733 rows, 54 features, 4 classes)
- **california-housing**: Real estate regression (20,640 rows, 8 features, continuous)

#### TabZilla Benchmark (20 datasets - "Hardest" Subset)
**Source**: TabZilla (https://github.com/naszilla/tabzilla) - NeurIPS 2023 benchmark
**Characteristics**:
- **Curated Difficulty**: Selected for challenging properties (class imbalance, high dimensionality, sparse data)
- **OpenML Integration**: Datasets sourced from OpenML-CC18 with task IDs
- **Reproducibility**: Fixed train/test splits, documented preprocessing

**Rationale for Dual Benchmarks**:
- **TabArena**: Represents "production-realistic" datasets enterprises encounter
- **TabZilla**: Stress-tests models on pathological cases revealing weaknesses

### Evaluation Metrics

**Primary Metrics** (reported in main results):

1. **ROC-AUC** (Binary & Multi-Class Classification)
   - Measures discrimination ability across all decision thresholds
   - Class-imbalance robust
   - Standard metric in TabArena, TabPFN, and ConTextTab papers

2. **Accuracy** (Classification)
   - Overall correct prediction rate
   - Interpretable for stakeholders
   - Comparable across all models

3. **F1-Score** (Classification)
   - Harmonic mean of precision and recall
   - Addresses class imbalance concerns
   - Important for enterprise use cases

4. **R² (Coefficient of Determination)** (Regression)
   - Proportion of variance explained
   - Standard regression metric
   - Negative values indicate worse-than-baseline performance

**Secondary Metrics** (reported in technical appendix):

5. **Training Time** (seconds)
   - Measures model development speed
   - Critical for enterprise time-to-value

6. **Inference Time** (milliseconds per prediction)
   - Measures production deployment feasibility
   - Important for real-time use cases

7. **Log Loss** (Classification)
   - Measures prediction confidence calibration
   - Penalizes overconfident incorrect predictions

8. **Memory Usage** (GB)
   - Peak RAM consumption during training
   - Infrastructure sizing consideration

### Experimental Protocol

**Cross-Validation Strategy**:
- **10-fold stratified cross-validation** for all classification tasks
- **10-fold cross-validation** for regression tasks
- **Stratification**: Maintains class distribution in each fold
- **Random Seed**: Fixed at 42 for reproducibility across all models
- **Aggregation**: Report mean ± standard deviation across folds

**Train/Test Splits**:
- **TabArena datasets**: Use cross-validation (no fixed test set)
- **TabZilla datasets**: Use predefined OpenML splits when available, otherwise cross-validation

**Handling Dataset-Specific Constraints**:
- **TabPFN limitations**: If dataset exceeds 10K rows or 500 features, subsample to TabPFN-compatible size and report separately
- **Memory constraints**: If model OOM on full dataset, use stratified subsample and document
- **Time limits**: Cap single model-dataset training at 4 hours; report timeout as failure mode

### Statistical Testing

**Friedman Test** (Primary):
- **Purpose**: Detect if statistically significant performance differences exist across models
- **Null Hypothesis**: All models perform equivalently across datasets
- **Significance Level**: α = 0.05
- **Interpretation**: Reject null if p < 0.05, indicating meaningful performance differences

**Nemenyi Post-Hoc Test**:
- **Purpose**: Pairwise comparison to identify which specific models differ significantly
- **Critical Difference**: Calculate CD based on number of models (7) and datasets (71)
- **Visualization**: Critical difference diagram showing model rankings

**Wilcoxon Signed-Rank Test** (Pairwise):
- **Purpose**: Direct pairwise comparison between RPT-1 and each competitor
- **Correction**: Bonferroni correction for multiple comparisons (α = 0.05 / 6 = 0.0083)
- **Effect Size**: Report Cohen's d for practical significance

**Robustness Checks**:
- **Sensitivity analysis**: Repeat with different random seeds (42, 123, 456)
- **Outlier analysis**: Identify datasets where all models struggle (outlier removal sensitivity)
- **Subgroup analysis**: Analyze performance by dataset size (<1K, 1K-10K, 10K-100K, >100K rows)

### Critical Difference Diagrams

Following Demšar (2006) methodology for visualizing statistical comparisons:

```
Average Rank (lower is better)
1      2      3      4      5      6      7
├──────┼──────┼──────┼──────┼──────┼──────┤
Model A ────────┐
Model B ────────┤ (no significant difference)
Model C ────────┘
         CD
Model D ──────────────────────────────────
```

**Interpretation**: Models connected by horizontal bar have no statistically significant difference.

---

## Pillar 3: Reproducibility & Transparency

### Docker-Based Frozen Environments

**Rationale**: Ensure exact replication by future researchers and eliminate "works on my machine" failures.

**Implementation**:

**1. Base Environment Dockerfile**
```dockerfile
FROM python:3.11-slim
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git wget build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies with pinned versions
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download datasets
COPY download_datasets.py .
RUN python download_datasets.py --output ./datasets
```

**2. Model-Specific Containers**
- `sap-rpt1:v1.0` - RPT-1 environment (Python 3.11, exact package versions)
- `tabpfn:v2.5` - TabPFN environment (Python 3.9, PriorLabs dependencies)
- `autogluon:v1.0` - AutoGluon environment (Python 3.8, MXNet/PyTorch)
- `gradient-boost:v1.0` - XGBoost/CatBoost/LightGBM environment

**3. Experiment Runner Container**
```bash
docker run --gpus all \
  -v $(pwd)/results:/workspace/results \
  -e DATASET=adult \
  -e MODEL=rpt1 \
  -e SEED=42 \
  sap-benchmarking:latest \
  python run_experiment.py
```

**Benefits**:
- **Exact replication**: Same Python versions, package versions, CUDA versions
- **Isolation**: No dependency conflicts between models
- **Portability**: Run on any machine with Docker + GPU
- **Archival**: Frozen containers enable replication years later

### Public GitHub Repository

**Repository Structure**:
```
sap-rpt1-benchmarking/
├── README.md (setup instructions, results summary)
├── requirements.txt (pinned dependencies)
├── docker/
│   ├── Dockerfile.base
│   ├── Dockerfile.rpt1
│   ├── Dockerfile.tabpfn
│   └── Dockerfile.autogluon
├── src/
│   ├── models/ (wrappers for each model)
│   ├── datasets/ (download and preprocessing scripts)
│   ├── evaluation/ (metrics, cross-validation, statistical tests)
│   └── visualization/ (critical difference diagrams, plots)
├── experiments/
│   ├── run_experiment.py (single model-dataset run)
│   ├── run_all.py (orchestrate all experiments)
│   └── configs/ (YAML configs for each model)
├── results/
│   ├── raw/ (CSV files with fold-level results)
│   ├── aggregated/ (summary statistics)
│   └── statistical_tests/ (Friedman, Nemenyi outputs)
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_results_visualization.ipynb
│   └── 03_statistical_testing.ipynb
└── paper/
    ├── main.tex (LaTeX source for NeurIPS/ICML submission)
    └── figures/ (generated plots)
```

**Documentation Standards**:
- **README**: Step-by-step setup (5-minute quick start)
- **Code comments**: Docstrings for all functions
- **Reproducibility guide**: Exact commands to replicate results
- **Dataset manifest**: URLs, checksums, licenses for all 71 datasets
- **Compute tracking**: Log GPU hours, costs, carbon footprint

### REFORMS Checklist Compliance

**REFORMS** (Reporting Standards for Machine Learning Based Science):

✅ **R - Random Seeds**: All random seeds documented (NumPy: 42, PyTorch: 42, XGBoost: 42)
✅ **E - Error Bars**: Report mean ± std across 10 cross-validation folds
✅ **F - Failed Experiments**: Document timeout/OOM failures in appendix
✅ **O - Outliers**: Report outlier datasets where all models struggle
✅ **R - Reproducibility**: Docker containers + GitHub repo
✅ **M - Multiple Comparisons**: Bonferroni correction for pairwise tests
✅ **S - Statistical Significance**: Friedman + Nemenyi tests with p-values

### Compute Cost Transparency

**Primary Resource**: UW Tillicum H200 80GB GPUs
- **Cost**: $0.90 per GPU hour
- **Estimated Usage**: 120 hours (moderate scenario)
- **Estimated Cost**: $108

**Cost Breakdown by Phase**:
```
Dataset Downloads:        2 hours    $  1.80
RPT-1 Experiments:       30 hours    $ 27.00
TabPFN Experiments:      15 hours    $ 13.50
TabICL Experiments:      20 hours    $ 18.00
AutoGluon Experiments:   25 hours    $ 22.50
Traditional ML:          15 hours    $ 13.50
Statistical Analysis:     5 hours    $  4.50
Result Aggregation:       8 hours    $  7.20
─────────────────────────────────────────
TOTAL:                  120 hours    $108.00
```

**Transparency Commitment**:
- Log actual GPU hours per experiment
- Report cost overruns with explanations
- Publish carbon footprint estimate (CodeCarbon library)

### Data Availability Statement

**Datasets**:
- All 71 datasets sourced from **public repositories** (TabArena, TabZilla, OpenML)
- **No proprietary data** used
- **Licenses**: Verified all datasets permit academic research and redistribution
- **Download script**: Automated retrieval with checksums for integrity

**Code**:
- **License**: MIT License (permissive open-source)
- **Dependencies**: All open-source (PyTorch, scikit-learn, XGBoost, etc.)
- **No vendor lock-in**: Runs on any cloud provider or on-premises hardware

---

## Experimental Workflow

### Phase-by-Phase Execution

**Phase 1: Infrastructure Setup** (Week 4-5)
- Set up UW Tillicum account and GPU allocation
- Build Docker containers for all models
- Validate environments with "hello world" experiments
- **Deliverable**: All 7 models successfully run on 1 test dataset

**Phase 2: Dataset Preparation** (Week 5)
- Download all 71 datasets from TabArena, TabZilla, OpenML
- Verify checksums and data integrity
- Preprocess (handle missing values, encode categoricals per model requirements)
- Generate train/test splits and cross-validation folds
- **Deliverable**: Dataset manifest with metadata (rows, features, task type)

**Phase 3: Baseline Experiments** (Week 6)
- Run XGBoost, CatBoost, LightGBM on all 71 datasets
- Validate experimental pipeline (metrics calculation, logging, error handling)
- **Deliverable**: Baseline results establishing performance floor

**Phase 4: Foundation Model Experiments** (Week 7-9)
- Run SAP RPT-1 on all 71 datasets (Week 7)
- Run TabPFN on compatible datasets (Week 8)
- Run TabICL on all 71 datasets (Week 8)
- Run AutoGluon on all 71 datasets (Week 9)
- **Deliverable**: Complete results matrix (7 models × 71 datasets)

**Phase 5: Statistical Analysis** (Week 10)
- Aggregate cross-validation results
- Friedman test across all models
- Nemenyi post-hoc pairwise comparisons
- Generate critical difference diagrams
- Subgroup analyses (by dataset size, domain, etc.)
- **Deliverable**: Statistical test results with significance levels

**Phase 6: Paper Writing** (Week 11-12)
- Draft NeurIPS/ICML paper (introduction, related work, methodology, results, discussion)
- Generate figures (performance plots, critical difference diagrams)
- Write technical appendix with per-dataset results
- Internal review and revision
- **Deliverable**: Paper draft ready for SAP review and conference submission

### Quality Assurance

**Code Review**:
- All experiment code peer-reviewed by team members
- Unit tests for metrics calculation (validate against scikit-learn)
- Integration tests for Docker environments

**Data Quality**:
- Checksum validation on all dataset downloads
- Exploratory data analysis to detect anomalies
- Cross-reference dataset statistics with published papers

**Results Validation**:
- Sanity checks (baseline models match published benchmarks)
- Outlier investigation (datasets where results seem anomalous)
- Reproducibility test (re-run random subset with different seed)

---

## Risk Mitigation

**Risk 1: Model Installation Failures**
- **Mitigation**: Test all model installations in Week 4; Docker isolation prevents conflicts
- **Contingency**: If model unavailable, document exclusion and justify

**Risk 2: Dataset Download Issues**
- **Mitigation**: Download scripts with retry logic; verify checksums
- **Contingency**: TabArena provides stable API; TabZilla archived on Zenodo

**Risk 3: Compute Resource Unavailability**
- **Mitigation**: Apply for UW Tillicum access early; secure backup AWS/Azure credits
- **Contingency**: Scale down to 40-50 datasets if compute limited; prioritize TabArena

**Risk 4: Experiment Runtime Overruns**
- **Mitigation**: Set 4-hour timeout per model-dataset pair; monitor progress daily
- **Contingency**: Report timeouts as failure mode; analyze in appendix

**Risk 5: Statistical Significance Not Achieved**
- **Mitigation**: 71 datasets provide high statistical power
- **Contingency**: If no significant differences, report as "RPT-1 competitive but not superior"

---

## Alignment with Publication Standards

**NeurIPS/ICML Requirements**:
✅ **Novel Contribution**: First comprehensive independent RPT-1 benchmark
✅ **Reproducibility**: Code, data, Docker environments public
✅ **Statistical Rigor**: Friedman/Nemenyi tests standard in ML benchmarking
✅ **Broad Evaluation**: 71 datasets exceeds typical benchmarking papers (20-40 datasets)
✅ **Transparency**: Report all results (including failures)

**Related Work Comparison**:
- **TabPFN (Nature 2025)**: 30 datasets, 5 baselines → Our study: 71 datasets, 7 models
- **ConTextTab (NeurIPS 2025)**: ~15-20 datasets, limited competitors → Our study: comprehensive coverage
- **TabZilla (NeurIPS 2023)**: 36 datasets, standardized splits → We extend with TabArena

**Differentiation**: Our study is the **first** to evaluate RPT-1 independently at scale with statistical rigor.

---

## Conclusion

Our three-pillar methodology ensures this benchmarking study meets the highest academic standards while delivering actionable insights for SAP. By combining **comprehensive model coverage** (7 models across 71 datasets), **statistical rigor** (Friedman/Nemenyi tests with proper multiple comparison correction), and **reproducibility** (Docker, GitHub, REFORMS compliance), we provide credible third-party validation suitable for NeurIPS/ICML publication and enterprise decision-making.

---

**Document Version**: 1.0
**Last Updated**: November 8, 2025
**Classification**: Proposal - Methodology & Experimental Design

**References**:
- Demšar, J. (2006). Statistical comparisons of classifiers over multiple data sets. Journal of Machine Learning Research, 7, 1-30.
- Hollmann, N., Müller, S., & Hutter, F. (2025). Accurate predictions on small data with a tabular foundation model. Nature.
- Spinaci, M., et al. (2025). ConTextTab: A Semantics-Aware Tabular In-Context Learner. NeurIPS 2025.
- AutoGluon Team. (2025). TabArena: A Living Benchmark for Tabular Prediction. arXiv:2506.16791.
