"""
Evaluation Metrics
==================

Comprehensive metrics for classification and regression tasks.

Author: UW MSIM Team
Date: November 2025
"""

import numpy as np
from sklearn.metrics import (
    roc_auc_score, accuracy_score, f1_score, precision_score, recall_score,
    r2_score, mean_squared_error, mean_absolute_error, log_loss
)
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)


def calculate_classification_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_proba: Optional[np.ndarray] = None
) -> Dict[str, float]:
    """
    Calculate all classification metrics.

    Parameters
    ----------
    y_true : np.ndarray
        True labels
    y_pred : np.ndarray
        Predicted labels
    y_proba : np.ndarray, optional
        Predicted probabilities (n_samples, n_classes)

    Returns
    -------
    metrics : dict
        Dictionary of metric names and values
    """
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'f1_macro': f1_score(y_true, y_pred, average='macro', zero_division=0),
        'f1_weighted': f1_score(y_true, y_pred, average='weighted', zero_division=0),
        'precision_macro': precision_score(y_true, y_pred, average='macro', zero_division=0),
        'recall_macro': recall_score(y_true, y_pred, average='macro', zero_division=0)
    }

    # ROC-AUC (if probabilities available)
    if y_proba is not None:
        try:
            n_classes = len(np.unique(y_true))

            if n_classes == 2:
                # Binary classification
                metrics['roc_auc'] = roc_auc_score(y_true, y_proba[:, 1])
            else:
                # Multi-class classification
                metrics['roc_auc'] = roc_auc_score(
                    y_true, y_proba,
                    multi_class='ovr',
                    average='macro'
                )

            # Log loss
            metrics['log_loss'] = log_loss(y_true, y_proba)

        except Exception as e:
            logger.warning(f"ROC-AUC calculation failed: {e}")
            metrics['roc_auc'] = np.nan
            metrics['log_loss'] = np.nan

    return metrics


def calculate_regression_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray
) -> Dict[str, float]:
    """
    Calculate all regression metrics.

    Parameters
    ----------
    y_true : np.ndarray
        True values
    y_pred : np.ndarray
        Predicted values

    Returns
    -------
    metrics : dict
        Dictionary of metric names and values
    """
    metrics = {
        'r2': r2_score(y_true, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
        'mae': mean_absolute_error(y_true, y_pred),
        'mse': mean_squared_error(y_true, y_pred)
    }

    # MAPE (avoid division by zero)
    try:
        non_zero_mask = y_true != 0
        if np.any(non_zero_mask):
            mape = np.mean(np.abs((y_true[non_zero_mask] - y_pred[non_zero_mask]) / y_true[non_zero_mask])) * 100
            metrics['mape'] = mape
        else:
            metrics['mape'] = np.nan
    except:
        metrics['mape'] = np.nan

    return metrics
