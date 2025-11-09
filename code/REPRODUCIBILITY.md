# Reproducibility Checklist

This benchmarking codebase follows NeurIPS/ICML reproducibility standards.

## ✅ Environment Reproducibility

- [x] **Docker containers**: Separate containers for incompatible Python versions
- [x] **Frozen dependencies**: `requirements-*.txt` with pinned versions
- [x] **Random seeds**: Fixed seeds throughout (default: 42)
- [x] **Hardware specs**: GPU type, memory, CPU cores logged

## ✅ Data Reproducibility

- [x] **Dataset downloads**: Automated via OpenML API with task IDs
- [x] **Data splits**: Stratified k-fold CV with fixed random state
- [x] **Preprocessing**: Minimal, documented, deterministic
- [x] **Data catalog**: Complete metadata for all datasets

## ✅ Model Reproducibility

- [x] **Model versions**: Exact versions specified in requirements
- [x] **Hyperparameters**: Logged in config files and experiment outputs
- [x] **Training procedures**: Documented in model wrappers
- [x] **Inference**: Consistent prediction protocols

## ✅ Evaluation Reproducibility

- [x] **Metrics**: Standard sklearn metrics, clearly defined
- [x] **Cross-validation**: 10-fold stratified, fixed random state
- [x] **Statistical tests**: Friedman + Nemenyi with p-values
- [x] **Aggregation**: Mean ± std across folds

## ✅ Computational Reproducibility

- [x] **Compute tracking**: GPU hours, wall-clock time, costs
- [x] **Resource limits**: Memory limits, timeouts specified
- [x] **Platform**: UW Tillicum (H200 GPUs) or equivalent
- [x] **Cost estimates**: Transparent cost reporting

## ✅ Code Reproducibility

- [x] **Version control**: Git repository with complete history
- [x] **Documentation**: README, docstrings, inline comments
- [x] **Installation**: One-command setup via `pip install -e .`
- [x] **Testing**: Unit tests for critical components (TODO)

## 🔄 How to Reproduce Results

### 1. Setup Environment

```bash
# Clone repository
git clone [repo-url]
cd code

# Build Docker images
docker-compose build

# Or install locally (if compatible Python version)
pip install -e .
```

### 2. Download Datasets

```bash
# Download TabArena datasets (51 datasets)
python -m datasets.download_tabarena

# Create dataset catalog
python -m datasets.dataset_catalog
```

### 3. Run Single Experiment

```bash
# Run SAP RPT-1 on adult dataset
docker-compose run sap-rpt1 -m runners.run_experiment \
    --dataset adult \
    --model sap-rpt1-small \
    --config config/experiments.yaml
```

### 4. Run Full Benchmark

```bash
# Run all models on all datasets
docker-compose run baselines -m runners.run_batch \
    --datasets config/datasets.yaml \
    --models config/models.yaml
```

### 5. Analyze Results

```bash
# Aggregate results
python -m analysis.aggregate_results

# Statistical tests
python -m analysis.statistical_analysis

# Generate visualizations
python -m analysis.visualizations
```

## 📊 Expected Outputs

- **Raw results**: `results/raw/*.json` (one per experiment)
- **Aggregated results**: `results/processed/aggregated_results.csv`
- **Statistical tests**: `results/processed/statistical_tests.json`
- **Visualizations**: `results/processed/figures/*.png`
- **Compute logs**: `results/processed/compute_summary.csv`

## 🚨 Known Limitations

1. **Hardware dependence**: Results may vary slightly across GPUs
2. **Stochastic models**: Some models have inherent randomness
3. **Timeout effects**: Long-running models may hit time limits
4. **Memory constraints**: Large datasets may require >80GB GPU memory

## 📖 References

- **REFORMS Checklist**: https://reforms.cs.princeton.edu/
- **NeurIPS 2025 Guidelines**: [Conference CFP]
- **TabArena Paper**: McElfresh et al., NeurIPS 2024
- **SAP RPT-1 Paper**: ConTextTab (arXiv:2506.10707v4)

## 📧 Contact

For reproducibility questions, contact:
- Rahil M. Harihar (rahilharihar@uw.edu)
- Siddarth Bhave (sbhave@uw.edu)
