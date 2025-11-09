"""
TabArena Dataset Downloader
============================

Downloads the 51 TabArena datasets via OpenML API.

TabArena is a benchmarking suite for tabular models introduced
in the ConTextTab paper (SAP RPT-1).

Author: UW MSIM Team
Date: November 2025
"""

import os
import logging
from typing import List, Optional
import pandas as pd
from tqdm import tqdm

logger = logging.getLogger(__name__)

# TabArena task IDs (51 datasets from ConTextTab paper)
TABARENA_TASK_IDS = [
    3, 12, 31, 37, 50, 54, 151, 188, 334, 375,
    458, 469, 1036, 1038, 1040, 1046, 1049, 1050, 1053, 1063,
    1067, 1068, 1120, 1169, 1461, 1462, 1464, 1480, 1485, 1486,
    1487, 1489, 1494, 1497, 1501, 1510, 1570, 4134, 4135, 4538,
    6566, 9910, 9946, 9952, 9957, 9960, 9964, 9971, 9976, 9977,
    9978
]


def download_tabarena_datasets(
    output_dir: str = '../datasets/tabarena',
    task_ids: Optional[List[int]] = None,
    force_redownload: bool = False
) -> dict:
    """
    Download TabArena datasets from OpenML.

    Parameters
    ----------
    output_dir : str
        Directory to save datasets
    task_ids : list of int, optional
        Specific task IDs to download (default: all 51)
    force_redownload : bool
        If True, redownload even if files exist

    Returns
    -------
    results : dict
        Summary of downloads with successes and failures
    """
    try:
        import openml
    except ImportError:
        raise ImportError("Install OpenML with: pip install openml")

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    metadata_path = os.path.join(output_dir, 'metadata.csv')

    # Use default task IDs if none provided
    if task_ids is None:
        task_ids = TABARENA_TASK_IDS

    logger.info(f"Downloading {len(task_ids)} TabArena datasets to {output_dir}")

    results = {
        'success': [],
        'failed': [],
        'metadata': []
    }

    # Download each dataset
    for i, task_id in enumerate(tqdm(task_ids, desc="Downloading TabArena")):
        try:
            logger.info(f"[{i+1}/{len(task_ids)}] Downloading task {task_id}...")

            # Get task and dataset
            task = openml.tasks.get_task(task_id)
            dataset = task.get_dataset()

            # Generate clean dataset name
            dataset_name = dataset.name.replace(' ', '_').replace('/', '_').replace('-', '_')
            dataset_name = ''.join(c for c in dataset_name if c.isalnum() or c == '_')

            # Check if already exists
            X_path = os.path.join(output_dir, f"{dataset_name}_X.csv")
            y_path = os.path.join(output_dir, f"{dataset_name}_y.csv")

            if os.path.exists(X_path) and os.path.exists(y_path) and not force_redownload:
                logger.info(f"  ✓ Already exists: {dataset_name}, skipping")
                results['success'].append(task_id)
                continue

            # Load data
            X, y, categorical_indicator, attribute_names = dataset.get_data(
                dataset_format="dataframe",
                target=dataset.default_target_attribute
            )

            # Save features and target
            X.to_csv(X_path, index=False)
            y.to_csv(y_path, index=False, header=True)

            # Collect metadata
            metadata = {
                'task_id': task_id,
                'dataset_name': dataset_name,
                'original_name': dataset.name,
                'n_samples': X.shape[0],
                'n_features': X.shape[1],
                'task_type': 'classification' if task.task_type_id in [1, 2, 3] else 'regression',
                'n_classes': len(y.unique()) if task.task_type_id in [1, 2, 3] else None,
                'n_categorical': sum(categorical_indicator) if categorical_indicator else 0,
                'n_numerical': X.shape[1] - (sum(categorical_indicator) if categorical_indicator else 0)
            }
            results['metadata'].append(metadata)
            results['success'].append(task_id)

            logger.info(f"  ✓ Downloaded: {dataset_name} ({X.shape[0]} rows, {X.shape[1]} cols)")

        except Exception as e:
            logger.error(f"  ✗ Failed: Task {task_id} - {e}")
            results['failed'].append({'task_id': task_id, 'error': str(e)})

    # Save metadata
    if results['metadata']:
        metadata_df = pd.DataFrame(results['metadata'])
        metadata_df.to_csv(metadata_path, index=False)
        logger.info(f"Metadata saved to {metadata_path}")

    # Summary
    logger.info(f"\nDownload Summary:")
    logger.info(f"  Successful: {len(results['success'])}/{len(task_ids)}")
    logger.info(f"  Failed: {len(results['failed'])}/{len(task_ids)}")

    return results


if __name__ == "__main__":
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Download all TabArena datasets
    results = download_tabarena_datasets()

    print(f"\n✅ Download complete!")
    print(f"   Successful: {len(results['success'])}")
    print(f"   Failed: {len(results['failed'])}")
