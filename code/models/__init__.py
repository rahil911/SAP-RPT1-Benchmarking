"""
Model Wrappers Package
======================

Provides sklearn-compatible wrappers for all benchmarking models.

Available Models:
- SAP RPT-1 (sap_rpt1_wrapper)
- TabPFN (tabpfn_wrapper)
- TabICL (tabicl_wrapper)
- AutoGluon (autogluon_wrapper)
- XGBoost (baseline_wrappers)
- CatBoost (baseline_wrappers)
- LightGBM (baseline_wrappers)

All models implement the sklearn API:
    - fit(X, y)
    - predict(X)
    - predict_proba(X)  # for classification
"""

from .base_wrapper import BaseModelWrapper
from .sap_rpt1_wrapper import SAPRPT1Wrapper
from .tabpfn_wrapper import TabPFNWrapper
from .tabicl_wrapper import TabICLWrapper
from .autogluon_wrapper import AutoGluonWrapper
from .baseline_wrappers import XGBoostWrapper, CatBoostWrapper, LightGBMWrapper

__all__ = [
    'BaseModelWrapper',
    'SAPRPT1Wrapper',
    'TabPFNWrapper',
    'TabICLWrapper',
    'AutoGluonWrapper',
    'XGBoostWrapper',
    'CatBoostWrapper',
    'LightGBMWrapper'
]

__version__ = '1.0.0'
