"""
Single Experiment Runner
=========================

Run a single model on a single dataset.

Usage:
    python -m runners.run_experiment --dataset adult --model sap-rpt1

Author: UW MSIM Team
Date: November 2025
"""

import argparse
import json
import yaml
import logging
import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from models import *
from datasets.preprocessors import load_dataset
from datasets.dataset_catalog import DatasetCatalog
from evaluation import run_cross_validation, ComputeTracker

logger = logging.getLogger(__name__)


def get_model(model_name: str, task_type: str, config: dict):
    """
    Initialize model by name.

    Parameters
    ----------
    model_name : str
        Model identifier
    task_type : str
        'classification' or 'regression'
    config : dict
        Model configuration

    Returns
    -------
    model : BaseModelWrapper
        Initialized model
    """
    model_map = {
        'sap-rpt1': SAPRPT1Wrapper,
        'sap-rpt1-small': lambda **kwargs: SAPRPT1Wrapper(model_size='small', **kwargs),
        'sap-rpt1-large': lambda **kwargs: SAPRPT1Wrapper(model_size='large', **kwargs),
        'tabpfn': TabPFNWrapper,
        'tabicl': TabICLWrapper,
        'autogluon': AutoGluonWrapper,
        'xgboost': XGBoostWrapper,
        'catboost': CatBoostWrapper,
        'lightgbm': LightGBMWrapper
    }

    if model_name not in model_map:
        raise ValueError(f"Unknown model: {model_name}. Choose from {list(model_map.keys())}")

    model_class = model_map[model_name]
    model = model_class(task_type=task_type, **config.get('model_params', {}))

    logger.info(f"Initialized {model_name} for {task_type}")

    return model


def run_single_experiment(
    dataset_name: str,
    model_name: str,
    config: dict,
    output_dir: str = '../results/raw'
) -> dict:
    """
    Run experiment on single dataset with single model.

    Parameters
    ----------
    dataset_name : str
        Dataset name
    model_name : str
        Model name
    config : dict
        Experiment configuration
    output_dir : str
        Where to save results

    Returns
    -------
    summary : dict
        Experiment results
    """
    logger.info(f"\n{'='*60}")
    logger.info(f"Experiment: {model_name} on {dataset_name}")
    logger.info(f"{'='*60}\n")

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Start compute tracking
    tracker = ComputeTracker(
        cost_per_hour=config.get('cost_per_hour', 0.90),
        gpu_type=config.get('gpu_type', 'H200')
    )
    tracker.start()

    try:
        # Load dataset
        logger.info("Loading dataset...")
        dataset_path = config.get('dataset_path', f'../datasets/{dataset_name}')
        X, y, task_type = load_dataset(dataset_path)

        # Initialize model
        model = get_model(model_name, task_type, config)

        # Run cross-validation
        fold_results = run_cross_validation(
            model=model,
            X=X,
            y=y,
            task_type=task_type,
            n_folds=config.get('n_folds', 10),
            random_state=config.get('random_state', 42)
        )

        # Stop tracking
        compute_summary = tracker.stop()

        # Aggregate results
        import pandas as pd
        results_df = pd.DataFrame(fold_results)

        summary = {
            'dataset': dataset_name,
            'model': model_name,
            'task_type': task_type,
            'n_samples': len(X),
            'n_features': X.shape[1],
            'n_folds': config.get('n_folds', 10),
            'mean_metrics': results_df.mean().to_dict(),
            'std_metrics': results_df.std().to_dict(),
            'fold_results': fold_results,
            'compute': compute_summary
        }

        # Save results
        output_file = os.path.join(output_dir, f"{dataset_name}_{model_name}.json")
        with open(output_file, 'w') as f:
            json.dump(summary, f, indent=2)

        logger.info(f"\n✅ Results saved to {output_file}")

        # Print summary
        primary_metric = 'roc_auc' if task_type == 'classification' else 'r2'
        if primary_metric in summary['mean_metrics']:
            mean_val = summary['mean_metrics'][primary_metric]
            std_val = summary['std_metrics'][primary_metric]
            logger.info(f"\nPrimary Metric ({primary_metric}): {mean_val:.4f} ± {std_val:.4f}")

        return summary

    except Exception as e:
        logger.error(f"Experiment failed: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Parse arguments
    parser = argparse.ArgumentParser(description='Run single benchmarking experiment')
    parser.add_argument('--dataset', required=True, help='Dataset name')
    parser.add_argument('--model', required=True, help='Model name')
    parser.add_argument('--config', default='../config/experiments.yaml', help='Config file')
    parser.add_argument('--output-dir', default='../results/raw', help='Output directory')

    args = parser.parse_args()

    # Load config
    if os.path.exists(args.config):
        with open(args.config) as f:
            config = yaml.safe_load(f)
    else:
        config = {
            'n_folds': 10,
            'random_state': 42,
            'cost_per_hour': 0.90,
            'gpu_type': 'H200'
        }

    # Run experiment
    results = run_single_experiment(
        dataset_name=args.dataset,
        model_name=args.model,
        config=config,
        output_dir=args.output_dir
    )

    print("\n✅ Experiment complete!")
