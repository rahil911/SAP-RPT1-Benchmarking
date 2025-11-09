"""
Cross-Validation
================

10-fold stratified cross-validation for model evaluation.

Author: UW MSIM Team
Date: November 2025
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, KFold
from typing import List, Dict
import logging

from .metrics import calculate_classification_metrics, calculate_regression_metrics

logger = logging.getLogger(__name__)


def run_cross_validation(
    model,
    X: pd.DataFrame,
    y: pd.Series,
    task_type: str = 'classification',
    n_folds: int = 10,
    random_state: int = 42
) -> List[Dict]:
    """
    Run k-fold cross-validation.

    Parameters
    ----------
    model : BaseModelWrapper
        Model to evaluate (must have fit/predict methods)
    X : pd.DataFrame
        Features
    y : pd.Series
        Target
    task_type : str
        'classification' or 'regression'
    n_folds : int
        Number of folds
    random_state : int
        Random seed

    Returns
    -------
    fold_results : list of dict
        Results for each fold
    """
    logger.info(f"Running {n_folds}-fold CV for {model.__class__.__name__}")

    # Choose CV splitter
    if task_type == 'classification':
        cv = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=random_state)
    else:
        cv = KFold(n_splits=n_folds, shuffle=True, random_state=random_state)

    fold_results = []

    for fold_idx, (train_idx, val_idx) in enumerate(cv.split(X, y)):
        logger.info(f"  Fold {fold_idx + 1}/{n_folds}")

        # Split data
        X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

        # Fit model
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_val)
        y_proba = None
        if task_type == 'classification':
            try:
                y_proba = model.predict_proba(X_val)
            except:
                pass

        # Calculate metrics
        if task_type == 'classification':
            metrics = calculate_classification_metrics(y_val, y_pred, y_proba)
        else:
            metrics = calculate_regression_metrics(y_val, y_pred)

        # Add timing info
        metrics.update({
            'fold': fold_idx,
            'fit_time': model.fit_time,
            'predict_time': model.predict_time
        })

        fold_results.append(metrics)

    return fold_results
