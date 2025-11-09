"""
Statistical Tests
=================

Statistical significance testing for model comparisons.

Implements:
- Friedman test (non-parametric ANOVA)
- Nemenyi post-hoc test
- Critical difference calculation

Author: UW MSIM Team
Date: November 2025
"""

import numpy as np
import pandas as pd
from scipy import stats
from typing import Dict, Tuple
import logging

logger = logging.getLogger(__name__)


def friedman_test(results_df: pd.DataFrame) -> Dict:
    """
    Friedman test for comparing multiple models.

    Parameters
    ----------
    results_df : pd.DataFrame
        Rows = datasets, columns = models, values = metric scores

    Returns
    -------
    results : dict
        Test statistic, p-value, and significance
    """
    # Rank models for each dataset (higher is better)
    ranks = results_df.rank(axis=1, ascending=False)

    # Friedman test
    stat, p_value = stats.friedmanchisquare(*[ranks[col] for col in ranks.columns])

    logger.info(f"Friedman Test: statistic={stat:.4f}, p-value={p_value:.4e}")

    return {
        'statistic': stat,
        'p_value': p_value,
        'significant': p_value < 0.05,
        'avg_ranks': ranks.mean().to_dict()
    }


def nemenyi_post_hoc(results_df: pd.DataFrame) -> pd.DataFrame:
    """
    Nemenyi post-hoc test (pairwise comparisons).

    Parameters
    ----------
    results_df : pd.DataFrame
        Rows = datasets, columns = models, values = metric scores

    Returns
    -------
    p_values : pd.DataFrame
        Pairwise p-values
    """
    try:
        import scikit_posthocs as sp
        ranks = results_df.rank(axis=1, ascending=False)
        p_values = sp.posthoc_nemenyi_friedman(ranks.T)
        return p_values
    except ImportError:
        logger.error("scikit-posthocs not installed. Install with: pip install scikit-posthocs")
        raise


def critical_difference(
    n_datasets: int,
    n_models: int,
    alpha: float = 0.05
) -> float:
    """
    Calculate critical difference for CD diagrams.

    Parameters
    ----------
    n_datasets : int
        Number of datasets
    n_models : int
        Number of models
    alpha : float
        Significance level

    Returns
    -------
    cd : float
        Critical difference value
    """
    # Critical value from Nemenyi distribution
    # Approximation using normal distribution
    q_alpha = stats.norm.ppf(1 - alpha / 2)

    cd = q_alpha * np.sqrt((n_models * (n_models + 1)) / (6 * n_datasets))

    logger.info(f"Critical Difference: {cd:.4f} (alpha={alpha})")

    return cd
