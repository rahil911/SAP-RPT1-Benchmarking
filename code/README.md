# Benchmarking Code Repository - Agent 4 (Infrastructure Engineer)

**Agent**: Agent 4 - Infrastructure Engineer
**Status**: ⏳ Awaiting Deployment
**Dependencies**:
- ✅ Research files complete (research/)
- ⏳ Project requirements defined (project-requirements.json)
- ✅ Compute resources documented (research/compute-resources-guide.md)
**Execution Mode**: Parallel with other agents (independent, no wait required)

---

## 🎯 Agent 4 Mission

Create a **production-ready, reproducible benchmarking codebase** for evaluating SAP RPT-1 and competing models across 70+ datasets. The code must meet academic publication standards (NeurIPS/ICML reproducibility requirements).

**Quality Target**: Publication-ready reproducibility
**Total Components**: 8 major sections + Docker configs
**Timeline**: Weeks 2-4 (parallel with content/visual creation)

---

## 📁 Repository Structure

```
code/
├── README.md (this file)
├── requirements.txt                    # Python dependencies
├── setup.py                            # Package installation
├── .gitignore                          # Git ignore rules
├── LICENSE                             # MIT License
│
├── docker/                             # 5 Docker environments
│   ├── sap-rpt1.Dockerfile            # Python 3.11 for SAP RPT-1
│   ├── tabpfn.Dockerfile              # Python 3.9+ for TabPFN
│   ├── tabicl.Dockerfile              # Python 3.9+ for TabICL
│   ├── autogluon.Dockerfile           # Python 3.8+ for AutoGluon
│   ├── baselines.Dockerfile           # Python 3.10 for XGBoost, CatBoost, LightGBM
│   └── docker-compose.yml             # Orchestration
│
├── config/                             # Configuration files
│   ├── datasets.yaml                  # Dataset specifications
│   ├── models.yaml                    # Model configurations
│   ├── metrics.yaml                   # Evaluation metrics
│   └── experiments.yaml               # Experiment settings
│
├── datasets/                           # Dataset management
│   ├── __init__.py
│   ├── download_tabarena.py           # TabArena downloader
│   ├── download_tabzilla.py           # TabZilla downloader
│   ├── download_openml.py             # OpenML downloader
│   ├── preprocessors.py               # Data preprocessing
│   └── dataset_catalog.py             # Dataset registry
│
├── models/                             # Model wrappers
│   ├── __init__.py
│   ├── base_wrapper.py                # sklearn-compatible base class
│   ├── sap_rpt1_wrapper.py            # SAP RPT-1 wrapper
│   ├── tabpfn_wrapper.py              # TabPFN wrapper
│   ├── tabicl_wrapper.py              # TabICL wrapper
│   ├── autogluon_wrapper.py           # AutoGluon wrapper
│   └── baseline_wrappers.py           # XGBoost, CatBoost, LightGBM
│
├── evaluation/                         # Evaluation tools
│   ├── __init__.py
│   ├── metrics.py                     # Metric calculations
│   ├── cross_validation.py            # CV protocols
│   ├── statistical_tests.py           # Friedman, Nemenyi, Wilcoxon
│   └── compute_tracker.py             # GPU hours, cost tracking
│
├── runners/                            # Experiment execution
│   ├── __init__.py
│   ├── run_experiment.py              # Single experiment runner
│   ├── run_batch.py                   # Batch experiments
│   ├── slurm_submit.py                # SLURM job submission (UW Tillicum)
│   └── checkpoint_manager.py          # Save/resume experiments
│
├── analysis/                           # Results analysis
│   ├── __init__.py
│   ├── aggregate_results.py           # Results aggregation
│   ├── statistical_analysis.py        # Statistical tests
│   ├── visualizations.py              # Critical difference diagrams, plots
│   └── report_generator.py            # Automated reporting
│
└── results/                            # Experiment outputs
    ├── raw/                           # Raw experiment logs
    ├── processed/                     # Aggregated results
    └── reports/                       # Generated reports
```

---

## 🐳 Docker Configurations (5 Environments)

### Why Docker?

**Reproducibility**: Different models require incompatible Python versions
- SAP RPT-1: Python 3.11 (strict requirement)
- TabPFN: Python 3.9+
- TabICL: Python 3.9+
- AutoGluon: Python 3.8+
- Baselines: Python 3.10 (optimal)

**Solution**: Separate Docker containers per model, orchestrated with docker-compose

---

### 1. sap-rpt1.Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install SAP RPT-1
RUN pip install --no-cache-dir \
    git+https://github.com/SAP-samples/sap-rpt-1-oss

# Install common dependencies
COPY requirements-sap-rpt1.txt .
RUN pip install --no-cache-dir -r requirements-sap-rpt1.txt

# Hugging Face authentication
# Note: Set HUGGING_FACE_HUB_TOKEN as environment variable
RUN pip install --no-cache-dir huggingface-hub

# Copy application code
COPY . /app

ENTRYPOINT ["python"]
```

**requirements-sap-rpt1.txt**:
```
numpy>=1.23.0
pandas>=1.5.0
scikit-learn>=1.2.0
torch>=2.0.0
transformers>=4.30.0
```

---

### 2. tabpfn.Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install TabPFN
RUN pip install --no-cache-dir tabpfn

COPY requirements-tabpfn.txt .
RUN pip install --no-cache-dir -r requirements-tabpfn.txt

COPY . /app

ENTRYPOINT ["python"]
```

**requirements-tabpfn.txt**:
```
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0
torch>=1.13.0
```

---

### 3. tabicl.Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install TabICL
RUN pip install --no-cache-dir tabicl

COPY requirements-tabicl.txt .
RUN pip install --no-cache-dir -r requirements-tabicl.txt

COPY . /app

ENTRYPOINT ["python"]
```

**requirements-tabicl.txt**:
```
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=1.0.0
torch>=2.0.0
```

---

### 4. autogluon.Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install AutoGluon Tabular
RUN pip install --no-cache-dir autogluon.tabular[all]

COPY requirements-autogluon.txt .
RUN pip install --no-cache-dir -r requirements-autogluon.txt

COPY . /app

ENTRYPOINT ["python"]
```

**requirements-autogluon.txt**:
```
numpy>=1.21.0
pandas>=1.4.0
scikit-learn>=1.0.0
```

---

### 5. baselines.Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install gradient boosting libraries
RUN pip install --no-cache-dir \
    xgboost \
    catboost \
    lightgbm \
    optuna

COPY requirements-baselines.txt .
RUN pip install --no-cache-dir -r requirements-baselines.txt

COPY . /app

ENTRYPOINT ["python"]
```

**requirements-baselines.txt**:
```
numpy>=1.21.0
pandas>=1.4.0
scikit-learn>=1.0.0
optuna>=3.0.0
```

---

### docker-compose.yml

```yaml
version: '3.8'

services:
  sap-rpt1:
    build:
      context: .
      dockerfile: docker/sap-rpt1.Dockerfile
    volumes:
      - ./datasets:/app/datasets:ro
      - ./results:/app/results
    environment:
      - HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  tabpfn:
    build:
      context: .
      dockerfile: docker/tabpfn.Dockerfile
    volumes:
      - ./datasets:/app/datasets:ro
      - ./results:/app/results
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  tabicl:
    build:
      context: .
      dockerfile: docker/tabicl.Dockerfile
    volumes:
      - ./datasets:/app/datasets:ro
      - ./results:/app/results
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  autogluon:
    build:
      context: .
      dockerfile: docker/autogluon.Dockerfile
    volumes:
      - ./datasets:/app/datasets:ro
      - ./results:/app/results
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]

  baselines:
    build:
      context: .
      dockerfile: docker/baselines.Dockerfile
    volumes:
      - ./datasets:/app/datasets:ro
      - ./results:/app/results
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

---

## 📦 Model Wrappers (sklearn-compatible)

### base_wrapper.py

```python
from abc import ABC, abstractmethod
from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
import time

class BaseModelWrapper(BaseEstimator, ABC):
    """
    Base class for all model wrappers
    Ensures sklearn-compatible interface for consistent evaluation
    """

    def __init__(self, task_type='classification'):
        self.task_type = task_type
        self.model = None
        self.fit_time = None
        self.predict_time = None

    @abstractmethod
    def fit(self, X, y):
        """Fit model on training data"""
        pass

    @abstractmethod
    def predict(self, X):
        """Make predictions"""
        pass

    def predict_proba(self, X):
        """Predict class probabilities (classification only)"""
        if self.task_type != 'classification':
            raise NotImplementedError("predict_proba only for classification")
        return self.model.predict_proba(X)

    def get_params(self, deep=True):
        """Get parameters (sklearn compatibility)"""
        return {'task_type': self.task_type}

    def set_params(self, **params):
        """Set parameters (sklearn compatibility)"""
        for key, value in params.items():
            setattr(self, key, value)
        return self
```

---

### sap_rpt1_wrapper.py

```python
from sap_rpt_1_oss import SAP_RPT_OSS_Classifier, SAP_RPT_OSS_Regressor
from .base_wrapper import BaseModelWrapper
import time

class SAPRPT1Wrapper(BaseModelWrapper):
    """
    Wrapper for SAP RPT-1-OSS
    """

    def __init__(self, task_type='classification', context_size=4096, bagging_factor=4):
        super().__init__(task_type)
        self.context_size = context_size
        self.bagging_factor = bagging_factor

        if task_type == 'classification':
            self.model = SAP_RPT_OSS_Classifier(
                context_size=context_size,
                bagging_factor=bagging_factor
            )
        else:
            self.model = SAP_RPT_OSS_Regressor(
                context_size=context_size,
                bagging_factor=bagging_factor
            )

    def fit(self, X, y):
        start = time.time()
        # SAP RPT-1 uses in-context learning (no training)
        # But fit() is called to conform to sklearn API
        self.model.fit(X, y)
        self.fit_time = time.time() - start
        return self

    def predict(self, X):
        start = time.time()
        predictions = self.model.predict(X)
        self.predict_time = time.time() - start
        return predictions

    def predict_proba(self, X):
        if self.task_type != 'classification':
            raise ValueError("predict_proba only for classification")
        return self.model.predict_proba(X)
```

---

### Similar wrappers for TabPFN, TabICL, AutoGluon, XGBoost, CatBoost, LightGBM

**(Pattern repeated with model-specific initialization and prediction logic)**

---

## 🔬 Evaluation Components

### metrics.py

```python
from sklearn.metrics import (
    roc_auc_score, accuracy_score, f1_score, precision_score, recall_score,
    r2_score, mean_squared_error, mean_absolute_error
)
import numpy as np

def calculate_classification_metrics(y_true, y_pred, y_proba=None):
    """
    Calculate all classification metrics
    """
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'f1_macro': f1_score(y_true, y_pred, average='macro'),
        'precision_macro': precision_score(y_true, y_pred, average='macro'),
        'recall_macro': recall_score(y_true, y_pred, average='macro')
    }

    # ROC-AUC (if probabilities available)
    if y_proba is not None:
        try:
            if y_proba.shape[1] == 2:  # Binary
                metrics['roc_auc'] = roc_auc_score(y_true, y_proba[:, 1])
            else:  # Multi-class
                metrics['roc_auc'] = roc_auc_score(
                    y_true, y_proba, multi_class='ovr', average='macro'
                )
        except Exception as e:
            print(f"ROC-AUC calculation failed: {e}")
            metrics['roc_auc'] = np.nan

    return metrics

def calculate_regression_metrics(y_true, y_pred):
    """
    Calculate all regression metrics
    """
    return {
        'r2': r2_score(y_true, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
        'mae': mean_absolute_error(y_true, y_pred),
        'mape': np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    }
```

---

### cross_validation.py

```python
from sklearn.model_selection import StratifiedKFold, KFold
import numpy as np

def run_cross_validation(model, X, y, task_type='classification', n_folds=10, random_state=42):
    """
    Run k-fold cross-validation
    """
    if task_type == 'classification':
        cv = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=random_state)
    else:
        cv = KFold(n_splits=n_folds, shuffle=True, random_state=random_state)

    fold_results = []

    for fold_idx, (train_idx, val_idx) in enumerate(cv.split(X, y)):
        X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

        # Fit model
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_val)
        y_proba = model.predict_proba(X_val) if task_type == 'classification' else None

        # Calculate metrics
        if task_type == 'classification':
            metrics = calculate_classification_metrics(y_val, y_pred, y_proba)
        else:
            metrics = calculate_regression_metrics(y_val, y_pred)

        # Add timing info
        metrics['fit_time'] = model.fit_time
        metrics['predict_time'] = model.predict_time

        fold_results.append(metrics)

    return fold_results
```

---

### statistical_tests.py

```python
from scipy.stats import friedmanchisquare, wilcoxon
from scikit_posthocs import posthoc_nemenyi_friedman
import pandas as pd
import numpy as np

def friedman_test(results_df):
    """
    Run Friedman test on model rankings
    results_df: rows=datasets, columns=models, values=metric scores
    """
    # Rank models for each dataset
    ranks = results_df.rank(axis=1, ascending=False)

    # Friedman test
    stat, p_value = friedmanchisquare(*[ranks[col] for col in ranks.columns])

    return {
        'statistic': stat,
        'p_value': p_value,
        'significant': p_value < 0.05
    }

def nemenyi_post_hoc(results_df):
    """
    Nemenyi post-hoc test (pairwise comparisons)
    """
    ranks = results_df.rank(axis=1, ascending=False)
    return posthoc_nemenyi_friedman(ranks.T)

def critical_difference(results_df, alpha=0.05):
    """
    Calculate critical difference for CD diagram
    """
    n_datasets = len(results_df)
    n_models = len(results_df.columns)

    # Critical value (from Nemenyi distribution)
    from scipy.stats import norm
    q_alpha = norm.ppf(1 - alpha / 2)

    cd = q_alpha * np.sqrt((n_models * (n_models + 1)) / (6 * n_datasets))
    return cd
```

---

## 🚀 Experiment Runners

### run_experiment.py

```python
import argparse
import json
import yaml
from models import SAPRPT1Wrapper, TabPFNWrapper, TabICLWrapper
from evaluation import run_cross_validation
from datasets import load_dataset
import pandas as pd

def run_single_experiment(dataset_name, model_name, config):
    """
    Run experiment on single dataset with single model
    """
    # Load dataset
    X, y, task_type = load_dataset(dataset_name)

    # Initialize model
    model = get_model(model_name, task_type, config)

    # Run CV
    results = run_cross_validation(
        model, X, y,
        task_type=task_type,
        n_folds=config['n_folds'],
        random_state=config['random_state']
    )

    # Aggregate results
    results_df = pd.DataFrame(results)
    summary = {
        'dataset': dataset_name,
        'model': model_name,
        'task_type': task_type,
        'mean_metrics': results_df.mean().to_dict(),
        'std_metrics': results_df.std().to_dict(),
        'fold_results': results
    }

    return summary

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', required=True)
    parser.add_argument('--model', required=True)
    parser.add_argument('--config', default='config/experiments.yaml')
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    results = run_single_experiment(args.dataset, args.model, config)

    # Save results
    output_path = f"results/raw/{args.dataset}_{args.model}.json"
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"✅ Results saved to {output_path}")
```

---

### run_batch.py

```python
import yaml
import subprocess
from itertools import product
from tqdm import tqdm

def run_batch_experiments(datasets, models, config_path):
    """
    Run experiments on all dataset×model combinations
    """
    experiments = list(product(datasets, models))

    results = []
    for dataset, model in tqdm(experiments, desc="Running experiments"):
        cmd = [
            'python', 'runners/run_experiment.py',
            '--dataset', dataset,
            '--model', model,
            '--config', config_path
        ]

        try:
            subprocess.run(cmd, check=True, capture_output=True)
            results.append({'dataset': dataset, 'model': model, 'status': 'success'})
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed: {dataset} × {model}")
            results.append({'dataset': dataset, 'model': model, 'status': 'failed', 'error': str(e)})

    return results

if __name__ == "__main__":
    with open('config/datasets.yaml') as f:
        datasets = yaml.safe_load(f)['datasets']

    with open('config/models.yaml') as f:
        models = yaml.safe_load(f)['models']

    results = run_batch_experiments(datasets, models, 'config/experiments.yaml')

    # Summary
    success_count = sum(1 for r in results if r['status'] == 'success')
    print(f"\n✅ Completed: {success_count}/{len(results)} experiments")
```

---

### slurm_submit.py (for UW Tillicum)

```python
#!/usr/bin/env python3
"""
SLURM job submission script for UW Tillicum
"""

SLURM_TEMPLATE = """#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --output=logs/{job_name}_%j.out
#SBATCH --error=logs/{job_name}_%j.err
#SBATCH --time={time_limit}
#SBATCH --partition=gpu
#SBATCH --gres=gpu:h200:1
#SBATCH --mem={memory}

# Load modules
module load python/3.11

# Activate virtual environment
source venv/bin/activate

# Run experiment
python runners/run_experiment.py --dataset {dataset} --model {model}
"""

def generate_slurm_script(dataset, model, time_limit="24:00:00", memory="64G"):
    """
    Generate SLURM submission script
    """
    job_name = f"{dataset}_{model}"
    script = SLURM_TEMPLATE.format(
        job_name=job_name,
        time_limit=time_limit,
        memory=memory,
        dataset=dataset,
        model=model
    )

    script_path = f"slurm_scripts/{job_name}.sh"
    with open(script_path, 'w') as f:
        f.write(script)

    return script_path

def submit_slurm_job(script_path):
    """
    Submit job to SLURM
    """
    import subprocess
    result = subprocess.run(['sbatch', script_path], capture_output=True, text=True)
    return result.stdout.strip()
```

---

## 📊 Analysis Tools

### aggregate_results.py

```python
import glob
import json
import pandas as pd

def aggregate_all_results(results_dir='results/raw'):
    """
    Aggregate all experiment results into single DataFrame
    """
    result_files = glob.glob(f"{results_dir}/*.json")

    aggregated = []
    for file in result_files:
        with open(file) as f:
            data = json.load(f)

        aggregated.append({
            'dataset': data['dataset'],
            'model': data['model'],
            **data['mean_metrics']
        })

    df = pd.DataFrame(aggregated)
    return df

if __name__ == "__main__":
    df = aggregate_all_results()
    df.to_csv('results/processed/aggregated_results.csv', index=False)
    print(f"✅ Aggregated {len(df)} experiment results")
```

---

## 📋 Configuration Files

### config/datasets.yaml

```yaml
datasets:
  tabarena:
    - adult
    - bank-marketing
    - california-housing
    # ... (51 total)

  tabzilla:
    - dataset_1
    - dataset_2
    # ... (20 subset)

  openml_cc18:
    - kr-vs-kp
    - vehicle
    # ... (15 subset)
```

### config/models.yaml

```yaml
models:
  - sap_rpt1_small
  - sap_rpt1_large
  - tabpfn
  - tabicl
  - autogluon
  - catboost
  - xgboost
  - lightgbm
```

### config/experiments.yaml

```yaml
experiment_settings:
  n_folds: 10
  random_state: 42
  timeout: 86400  # 24 hours

compute:
  gpu_memory_limit: 80  # GB
  checkpoint_interval: 3600  # 1 hour
```

---

## ✅ Deliverable Checklist

### Docker Infrastructure
- [ ] sap-rpt1.Dockerfile created
- [ ] tabpfn.Dockerfile created
- [ ] tabicl.Dockerfile created
- [ ] autogluon.Dockerfile created
- [ ] baselines.Dockerfile created
- [ ] docker-compose.yml created
- [ ] All Dockerfiles tested and building successfully

### Model Wrappers
- [ ] base_wrapper.py (sklearn-compatible base class)
- [ ] sap_rpt1_wrapper.py
- [ ] tabpfn_wrapper.py
- [ ] tabicl_wrapper.py
- [ ] autogluon_wrapper.py
- [ ] baseline_wrappers.py (XGBoost, CatBoost, LightGBM)
- [ ] All wrappers tested with sample data

### Evaluation Components
- [ ] metrics.py (classification & regression metrics)
- [ ] cross_validation.py (k-fold CV)
- [ ] statistical_tests.py (Friedman, Nemenyi, CD)
- [ ] compute_tracker.py (GPU hours, cost tracking)

### Experiment Runners
- [ ] run_experiment.py (single experiment)
- [ ] run_batch.py (batch experiments)
- [ ] slurm_submit.py (SLURM job submission)
- [ ] checkpoint_manager.py (save/resume)

### Analysis Tools
- [ ] aggregate_results.py
- [ ] statistical_analysis.py
- [ ] visualizations.py (CD diagrams, plots)
- [ ] report_generator.py

### Configuration
- [ ] datasets.yaml (71+ datasets)
- [ ] models.yaml (7+ models)
- [ ] metrics.yaml
- [ ] experiments.yaml

### Documentation
- [ ] README.md (this file) with setup instructions
- [ ] requirements.txt files for each Docker environment
- [ ] setup.py for package installation
- [ ] LICENSE (MIT)
- [ ] .gitignore

---

## 🚨 Critical Requirements

### Must-Do
- ✅ Use Docker for reproducibility (incompatible Python versions)
- ✅ sklearn-compatible interfaces for all models
- ✅ 10-fold stratified CV for all experiments
- ✅ Track compute time and GPU hours
- ✅ Checkpoint experiments (resume capability)
- ✅ Statistical rigor (Friedman, Nemenyi, CD)
- ✅ Comprehensive logging

### Must-NOT-Do
- ❌ Mix Python environments (use Docker only)
- ❌ Skip cross-validation
- ❌ Hardcode dataset paths (use config files)
- ❌ Ignore failures (log and report all errors)
- ❌ Lose experiment state (checkpoint regularly)

---

## 📊 Quality Standards

**Code Quality**: Publication-ready, PEP 8 compliant
**Reproducibility**: 100% (Docker + frozen environments)
**Test Coverage**: 80%+ (unit tests for all components)
**Documentation**: Comprehensive (docstrings + README)
**Timeline**: Weeks 2-4 (parallel development)

---

**Status**: ⏳ Awaiting Agent 4 deployment
**Owner**: Agent 4 (Infrastructure Engineer)
**Execution**: Parallel with Agents 1, 2, 3
**Next Step**: Deploy Agent 4 to build benchmarking codebase
