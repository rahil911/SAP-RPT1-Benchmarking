"""
AutoGluon Wrapper
=================

Sklearn-compatible wrapper for AutoGluon Tabular.

AutoGluon is an AutoML framework that automatically
trains and ensembles multiple models.

Author: UW MSIM Team
Date: November 2025
"""

import time
import logging
from typing import Optional, Union
import numpy as np
import pandas as pd
import tempfile
import shutil

from .base_wrapper import BaseModelWrapper

logger = logging.getLogger(__name__)


class AutoGluonWrapper(BaseModelWrapper):
    """
    AutoGluon Tabular wrapper.

    Parameters
    ----------
    task_type : str, default='classification'
        Task type: 'classification' or 'regression'
    time_limit : int, default=300
        Time limit for training in seconds
    preset : str, default='medium_quality'
        Preset: 'best_quality', 'high_quality', 'good_quality', 'medium_quality'
    eval_metric : str, optional
        Evaluation metric (auto-detected if None)
    random_state : int, default=42
        Random seed
    """

    def __init__(
        self,
        task_type: str = 'classification',
        time_limit: int = 300,
        preset: str = 'medium_quality',
        eval_metric: Optional[str] = None,
        random_state: int = 42
    ):
        super().__init__(task_type=task_type, random_state=random_state)
        self.time_limit = time_limit
        self.preset = preset
        self.eval_metric = eval_metric
        self._temp_dir = None

    def fit(self, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray]) -> 'AutoGluonWrapper':
        """
        Fit AutoGluon model.

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Training features
        y : pd.Series or np.ndarray, shape (n_samples,)
            Training target

        Returns
        -------
        self : AutoGluonWrapper
            Fitted model
        """
        self._validate_input(X, y)

        logger.info(f"Fitting AutoGluon ({self.preset}) on {X.shape[0]} samples...")
        start_time = time.time()

        try:
            from autogluon.tabular import TabularPredictor

            # Convert to DataFrame if needed
            if isinstance(X, np.ndarray):
                X = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])

            if isinstance(y, np.ndarray):
                y = pd.Series(y, name='target')

            # Combine X and y for AutoGluon
            train_data = X.copy()
            train_data['target'] = y.values

            # Create temporary directory for model
            self._temp_dir = tempfile.mkdtemp(prefix='autogluon_')

            # Auto-detect problem type
            problem_type = 'binary' if self.task_type == 'classification' and len(np.unique(y)) == 2 else None
            if self.task_type == 'regression':
                problem_type = 'regression'
            elif self.task_type == 'classification' and len(np.unique(y)) > 2:
                problem_type = 'multiclass'

            # Initialize predictor
            self.model = TabularPredictor(
                label='target',
                problem_type=problem_type,
                eval_metric=self.eval_metric,
                path=self._temp_dir,
                verbosity=2
            )

            # Fit model
            self.model.fit(
                train_data=train_data,
                time_limit=self.time_limit,
                presets=self.preset,
                random_state=self.random_state
            )

            self.is_fitted = True
            self.fit_time = time.time() - start_time

            # Log leaderboard
            leaderboard = self.model.leaderboard(silent=True)
            best_model = leaderboard.iloc[0]['model']
            logger.info(f"AutoGluon fitted in {self.fit_time:.2f} seconds. Best model: {best_model}")

        except ImportError:
            logger.error("AutoGluon not installed")
            raise ImportError("Install AutoGluon with: pip install autogluon.tabular[all]")
        except Exception as e:
            logger.error(f"Error fitting AutoGluon: {e}")
            raise

        return self

    def predict(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """
        Make predictions with AutoGluon.

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Test features

        Returns
        -------
        predictions : np.ndarray, shape (n_samples,)
            Predicted values or class labels
        """
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")

        self._validate_input(X)

        logger.info(f"Predicting on {X.shape[0]} samples with AutoGluon...")
        start_time = time.time()

        try:
            # Convert to DataFrame if needed
            if isinstance(X, np.ndarray):
                X = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])

            predictions = self.model.predict(X).values
            self.predict_time = time.time() - start_time

            logger.info(f"Predictions complete in {self.predict_time:.2f} seconds")

            return predictions

        except Exception as e:
            logger.error(f"Error during prediction: {e}")
            raise

    def _predict_proba_impl(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """
        Predict class probabilities with AutoGluon.

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Test features

        Returns
        -------
        probabilities : np.ndarray, shape (n_samples, n_classes)
            Class probabilities
        """
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])

        return self.model.predict_proba(X).values

    def get_params(self, deep: bool = True) -> dict:
        """Get parameters for this estimator."""
        params = super().get_params(deep)
        params.update({
            'time_limit': self.time_limit,
            'preset': self.preset,
            'eval_metric': self.eval_metric
        })
        return params

    def __del__(self):
        """Clean up temporary directory on deletion."""
        if self._temp_dir and self._temp_dir.startswith('/tmp'):
            try:
                shutil.rmtree(self._temp_dir)
            except:
                pass
