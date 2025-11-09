# Dataset Documentation

**Benchmark Datasets for SAP RPT-1 Evaluation**

This directory contains documentation for datasets used in the SAP RPT-1 benchmarking study.

---

## Dataset Sources

### TabArena (51 datasets)
**Description**: Living benchmark for tabular data with diverse real-world datasets
**Coverage**: Classification and regression tasks across multiple domains
**Characteristics**:
- Small (< 1K rows), medium (1K-10K), large (> 10K) datasets
- Various feature types (numerical, categorical, mixed)
- Imbalanced and balanced class distributions
- Missing value scenarios

**Domains**: Healthcare, finance, marketing, e-commerce, manufacturing, social science

**Download**: See [../code/datasets/download_tabarena.py](../code/datasets/download_tabarena.py)

---

### TabZilla (20 datasets)
**Description**: Curated subset of hardest tabular ML benchmarks
**Coverage**: Challenging classification tasks
**Selection Criteria**:
- High complexity (many features, complex relationships)
- Representative of real-world difficulty
- Previously published in academic literature

**Domains**: Bioinformatics, computer systems, physics, economics

**Download**: See [../code/datasets/download_tabzilla.py](../code/datasets/download_tabzilla.py)

---

### OpenML-CC18 (Subset)
**Description**: Standardized classification benchmark suite
**Coverage**: 18 curated datasets for reproducible comparisons
**Characteristics**:
- Community-vetted data quality
- Standardized train/test splits
- Established baseline results

**Download**: Available via OpenML Python API

---

## Dataset Characteristics

| Benchmark | Datasets | Task Types | Size Range | Domains |
|-----------|----------|------------|------------|---------|
| TabArena | 51 | Classification, Regression | 100 - 100K rows | 10+ domains |
| TabZilla | 20 | Classification | 1K - 50K rows | 5+ domains |
| OpenML-CC18 | 18 | Classification | 500 - 50K rows | Various |
| **Total** | **89** | **Both** | **100 - 100K** | **15+** |

---

## Data Preprocessing

All datasets undergo standardized preprocessing:
1. **Missing Value Handling**: Imputation or removal based on percentage
2. **Feature Encoding**: Label encoding for categoricals, normalization for numericals
3. **Train/Test Splits**: Stratified 80/20 or cross-validation
4. **Standardization**: Zero mean, unit variance for numerical features

**Implementation**: See [../code/datasets/preprocessors.py](../code/datasets/preprocessors.py)

---

## Dataset Catalog

Complete dataset metadata available in:
- [../code/datasets/dataset_catalog.py](../code/datasets/dataset_catalog.py)

Includes:
- Dataset name and source
- Number of rows and columns
- Task type (classification/regression)
- Domain and application area
- Missing value percentage
- Class balance (for classification)

---

## Usage in Benchmarking

Datasets are used to evaluate:
- **Accuracy**: Predictive performance across diverse tasks
- **Robustness**: Performance under varying data characteristics
- **Efficiency**: Training time and compute requirements
- **Generalization**: Cross-dataset transfer capabilities

**Statistical Testing**: Friedman test with Nemenyi post-hoc analysis across all datasets

---

## Data Storage

Datasets are **not stored in this repository** due to size constraints.

**Download Instructions**:
1. Navigate to [../code/](../code/)
2. Run dataset download scripts
3. Data will be stored in `code/results/` (gitignored)

---

**Prepared by**: University of Washington MSIM Team
**Last Updated**: November 2025
