"""
Evaluation Package
==================

Tools for model evaluation, statistical testing, and benchmarking.

Author: UW MSIM Team
Date: November 2025
"""

from .metrics import calculate_classification_metrics, calculate_regression_metrics
from .cross_validation import run_cross_validation
from .statistical_tests import friedman_test, nemenyi_post_hoc, critical_difference
from .compute_tracker import ComputeTracker

__all__ = [
    'calculate_classification_metrics',
    'calculate_regression_metrics',
    'run_cross_validation',
    'friedman_test',
    'nemenyi_post_hoc',
    'critical_difference',
    'ComputeTracker'
]
