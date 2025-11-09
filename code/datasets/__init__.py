"""
Dataset Management Package
===========================

Tools for downloading, preprocessing, and managing benchmark datasets.

Supported Benchmarks:
- TabArena (51 datasets via OpenML)
- TabZilla (36 datasets)
- OpenML-CC18 (subset for cross-validation)

Author: UW MSIM Team
Date: November 2025
"""

from .download_tabarena import download_tabarena_datasets
from .download_tabzilla import download_tabzilla_datasets
from .preprocessors import TabularPreprocessor
from .dataset_catalog import DatasetCatalog, create_catalog

__all__ = [
    'download_tabarena_datasets',
    'download_tabzilla_datasets',
    'TabularPreprocessor',
    'DatasetCatalog',
    'create_catalog'
]

__version__ = '1.0.0'
