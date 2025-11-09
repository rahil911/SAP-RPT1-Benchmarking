"""
Results Aggregation
===================

Aggregate all experiment results into summary tables.

Author: UW MSIM Team
Date: November 2025
"""

import glob
import json
import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)


def aggregate_all_results(
    results_dir: str = '../results/raw',
    output_file: str = '../results/processed/aggregated_results.csv'
) -> pd.DataFrame:
    """
    Aggregate all experiment results into single DataFrame.

    Parameters
    ----------
    results_dir : str
        Directory containing result JSON files
    output_file : str
        Where to save aggregated CSV

    Returns
    -------
    df : pd.DataFrame
        Aggregated results
    """
    logger.info(f"Aggregating results from {results_dir}")

    result_files = glob.glob(os.path.join(results_dir, '*.json'))
    logger.info(f"Found {len(result_files)} result files")

    aggregated = []

    for file in result_files:
        try:
            with open(file) as f:
                data = json.load(f)

            record = {
                'dataset': data['dataset'],
                'model': data['model'],
                'task_type': data['task_type'],
                'n_samples': data['n_samples'],
                'n_features': data['n_features'],
                'n_folds': data['n_folds']
            }

            # Add mean metrics
            for metric, value in data['mean_metrics'].items():
                record[f'mean_{metric}'] = value

            # Add std metrics
            for metric, value in data['std_metrics'].items():
                record[f'std_{metric}'] = value

            # Add compute info
            if 'compute' in data:
                record['elapsed_hours'] = data['compute'].get('elapsed_hours')
                record['cost_usd'] = data['compute'].get('cost_usd')

            aggregated.append(record)

        except Exception as e:
            logger.warning(f"Failed to process {file}: {e}")

    # Create DataFrame
    df = pd.DataFrame(aggregated)

    # Save
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)

    logger.info(f"Aggregated {len(df)} results to {output_file}")

    return df


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    df = aggregate_all_results()

    print(f"\n✅ Aggregated {len(df)} experiment results")
    print(f"\nDatasets: {df['dataset'].nunique()}")
    print(f"Models: {df['model'].nunique()}")
    print(f"\nSample of results:")
    print(df.head())
