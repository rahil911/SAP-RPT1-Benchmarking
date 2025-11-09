# SAP RPT-1 Benchmarking - Quick Start Guide

## 🚀 Setup (5 minutes)

### Option 1: Docker (Recommended)

```bash
# Build all environments
cd code
docker-compose build

# Verify builds
docker-compose ps
```

### Option 2: Local Install

```bash
# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package
pip install -e .

# Install model dependencies
pip install -e ".[models]"
```

## 📊 Download Datasets (10 minutes)

```bash
# Download TabArena datasets (51 datasets via OpenML)
python -m datasets.download_tabarena

# Create catalog
python -m datasets.dataset_catalog
```

## 🧪 Run Single Experiment (2-10 minutes)

```bash
# Using Docker
docker-compose run sap-rpt1 -m runners.run_experiment \
    --dataset adult \
    --model sap-rpt1-small

# Using local install
python -m runners.run_experiment \
    --dataset adult \
    --model sap-rpt1-small
```

## 📈 View Results

Results are saved to `results/raw/[dataset]_[model].json`

Example output:
```json
{
  "dataset": "adult",
  "model": "sap-rpt1-small",
  "task_type": "classification",
  "mean_metrics": {
    "roc_auc": 0.8523,
    "accuracy": 0.8145
  },
  "compute": {
    "elapsed_hours": 0.25,
    "cost_usd": 0.225
  }
}
```

## 🔁 Run Full Benchmark

```bash
# All models on all datasets
python -m runners.run_batch \
    --datasets config/datasets.yaml \
    --models config/models.yaml
```

## 📊 Analyze Results

```bash
# Aggregate all results
python -m analysis.aggregate_results

# View aggregated results
cat results/processed/aggregated_results.csv
```

## 🏗️ Project Structure

```
code/
├── docker/              # Docker environments (5 containers)
├── models/              # Model wrappers (sklearn-compatible)
├── datasets/            # Dataset download & preprocessing
├── evaluation/          # Metrics, CV, statistical tests
├── runners/             # Experiment execution
├── analysis/            # Results aggregation & visualization
├── config/              # YAML configurations
├── utils/               # Logging, compute tracking
└── results/             # Experiment outputs
```

## 📚 Next Steps

1. **Full documentation**: See main `README.md`
2. **Reproducibility**: See `REPRODUCIBILITY.md`
3. **Model details**: See `models/README.md`
4. **Dataset info**: See `datasets/README.md`

## 🆘 Troubleshooting

**Docker build fails:**
```bash
# Clear cache and rebuild
docker-compose build --no-cache
```

**Out of memory:**
```bash
# Reduce batch size or use smaller model
docker-compose run sap-rpt1 -m runners.run_experiment \
    --dataset small_dataset \
    --model sap-rpt1-small
```

**Import errors:**
```bash
# Ensure package is installed
pip install -e .
```

## 📧 Support

Contact: rahilharihar@uw.edu, sbhave@uw.edu
