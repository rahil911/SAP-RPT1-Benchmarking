"""
Dataset Catalog
===============

Generate and manage catalog of all available datasets.

Author: UW MSIM Team
Date: November 2025
"""

import os
import pandas as pd
import logging
from typing import List, Dict
from pathlib import Path

logger = logging.getLogger(__name__)


class DatasetCatalog:
    """
    Catalog of all benchmarking datasets.

    Provides:
    - List of available datasets
    - Dataset statistics
    - Filtering by task type, size, etc.
    """

    def __init__(self, catalog_path: str = '../datasets/catalog.csv'):
        """
        Initialize dataset catalog.

        Parameters
        ----------
        catalog_path : str
            Path to catalog CSV file
        """
        self.catalog_path = catalog_path

        if os.path.exists(catalog_path):
            self.catalog = pd.read_csv(catalog_path)
            logger.info(f"Loaded catalog with {len(self.catalog)} datasets")
        else:
            self.catalog = pd.DataFrame()
            logger.warning(f"Catalog not found at {catalog_path}. Run create_catalog() first.")

    def get_datasets(
        self,
        task_type: str = None,
        min_samples: int = None,
        max_samples: int = None,
        min_features: int = None,
        max_features: int = None
    ) -> pd.DataFrame:
        """
        Get filtered list of datasets.

        Parameters
        ----------
        task_type : str, optional
            Filter by 'classification' or 'regression'
        min_samples : int, optional
            Minimum number of samples
        max_samples : int, optional
            Maximum number of samples
        min_features : int, optional
            Minimum number of features
        max_features : int, optional
            Maximum number of features

        Returns
        -------
        filtered : pd.DataFrame
            Filtered dataset catalog
        """
        filtered = self.catalog.copy()

        if task_type:
            filtered = filtered[filtered['task_type'] == task_type]

        if min_samples:
            filtered = filtered[filtered['n_samples'] >= min_samples]

        if max_samples:
            filtered = filtered[filtered['n_samples'] <= max_samples]

        if min_features:
            filtered = filtered[filtered['n_features'] >= min_features]

        if max_features:
            filtered = filtered[filtered['n_features'] <= max_features]

        return filtered

    def summary(self) -> dict:
        """Get summary statistics of catalog."""
        if self.catalog.empty:
            return {}

        return {
            'total_datasets': len(self.catalog),
            'classification': len(self.catalog[self.catalog['task_type'] == 'classification']),
            'regression': len(self.catalog[self.catalog['task_type'] == 'regression']),
            'total_samples': self.catalog['n_samples'].sum(),
            'avg_samples': self.catalog['n_samples'].mean(),
            'avg_features': self.catalog['n_features'].mean()
        }


def create_catalog(
    dataset_dirs: List[str],
    output_path: str = '../datasets/catalog.csv'
) -> pd.DataFrame:
    """
    Create dataset catalog from directories.

    Parameters
    ----------
    dataset_dirs : list of str
        List of directories containing datasets
    output_path : str
        Where to save catalog CSV

    Returns
    -------
    catalog : pd.DataFrame
        Dataset catalog
    """
    logger.info(f"Creating catalog from {len(dataset_dirs)} directories...")

    all_datasets = []

    for dataset_dir in dataset_dirs:
        if not os.path.exists(dataset_dir):
            logger.warning(f"Directory not found: {dataset_dir}, skipping")
            continue

        # Look for metadata.csv
        metadata_path = os.path.join(dataset_dir, 'metadata.csv')
        if os.path.exists(metadata_path):
            metadata = pd.read_csv(metadata_path)
            metadata['source_dir'] = dataset_dir
            all_datasets.append(metadata)
            logger.info(f"Added {len(metadata)} datasets from {dataset_dir}")
        else:
            logger.warning(f"No metadata.csv found in {dataset_dir}")

    if all_datasets:
        catalog = pd.concat(all_datasets, ignore_index=True)

        # Save catalog
        catalog.to_csv(output_path, index=False)
        logger.info(f"Catalog saved to {output_path} with {len(catalog)} datasets")

        return catalog
    else:
        logger.error("No datasets found")
        return pd.DataFrame()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Create catalog from TabArena and TabZilla
    catalog = create_catalog(
        dataset_dirs=[
            '../datasets/tabarena',
            '../datasets/tabzilla'
        ],
        output_path='../datasets/catalog.csv'
    )

    # Print summary
    if not catalog.empty:
        dc = DatasetCatalog('../datasets/catalog.csv')
        summary = dc.summary()
        print("\nDataset Catalog Summary:")
        for key, value in summary.items():
            print(f"  {key}: {value}")
