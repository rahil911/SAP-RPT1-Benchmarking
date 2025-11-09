"""
Baseline Model Wrappers
========================

Sklearn-compatible wrappers for traditional gradient boosting models:
- XGBoost
- CatBoost
- LightGBM

Author: UW MSIM Team
Date: November 2025
"""

import time
import logging
from typing import Optional, Union, Dict, Any
import numpy as np
import pandas as pd

from .base_wrapper import BaseModelWrapper

logger = logging.getLogger(__name__)


class XGBoostWrapper(BaseModelWrapper):
    """
    XGBoost wrapper.

    Parameters
    ----------
    task_type : str, default='classification'
        Task type: 'classification' or 'regression'
    n_estimators : int, default=100
        Number of boosting rounds
    learning_rate : float, default=0.1
        Step size shrinkage
    max_depth : int, default=6
        Maximum tree depth
    random_state : int, default=42
        Random seed
    **kwargs : dict
        Additional XGBoost parameters
    """

    def __init__(
        self,
        task_type: str = 'classification',
        n_estimators: int = 100,
        learning_rate: float = 0.1,
        max_depth: int = 6,
        random_state: int = 42,
        **kwargs
    ):
        super().__init__(task_type=task_type, random_state=random_state)
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.kwargs = kwargs

    def fit(self, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray]) -> 'XGBoostWrapper':
        """Fit XGBoost model."""
        self._validate_input(X, y)

        logger.info(f"Fitting XGBoost on {X.shape[0]} samples...")
        start_time = time.time()

        try:
            import xgboost as xgb

            if self.task_type == 'classification':
                self.model = xgb.XGBClassifier(
                    n_estimators=self.n_estimators,
                    learning_rate=self.learning_rate,
                    max_depth=self.max_depth,
                    random_state=self.random_state,
                    **self.kwargs
                )
            else:
                self.model = xgb.XGBRegressor(
                    n_estimators=self.n_estimators,
                    learning_rate=self.learning_rate,
                    max_depth=self.max_depth,
                    random_state=self.random_state,
                    **self.kwargs
                )

            self.model.fit(X, y)

            self.is_fitted = True
            self.fit_time = time.time() - start_time

            logger.info(f"XGBoost fitted in {self.fit_time:.2f} seconds")

        except ImportError:
            raise ImportError("Install XGBoost with: pip install xgboost")
        except Exception as e:
            logger.error(f"Error fitting XGBoost: {e}")
            raise

        return self

    def predict(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Make predictions with XGBoost."""
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")

        self._validate_input(X)

        start_time = time.time()
        predictions = self.model.predict(X)
        self.predict_time = time.time() - start_time

        return predictions

    def _predict_proba_impl(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Predict class probabilities."""
        return self.model.predict_proba(X)

    def get_params(self, deep: bool = True) -> dict:
        """Get parameters."""
        params = super().get_params(deep)
        params.update({
            'n_estimators': self.n_estimators,
            'learning_rate': self.learning_rate,
            'max_depth': self.max_depth,
            **self.kwargs
        })
        return params


class CatBoostWrapper(BaseModelWrapper):
    """
    CatBoost wrapper.

    Parameters
    ----------
    task_type : str, default='classification'
        Task type: 'classification' or 'regression'
    iterations : int, default=100
        Number of boosting iterations
    learning_rate : float, default=0.1
        Step size shrinkage
    depth : int, default=6
        Tree depth
    random_state : int, default=42
        Random seed
    **kwargs : dict
        Additional CatBoost parameters
    """

    def __init__(
        self,
        task_type: str = 'classification',
        iterations: int = 100,
        learning_rate: float = 0.1,
        depth: int = 6,
        random_state: int = 42,
        **kwargs
    ):
        super().__init__(task_type=task_type, random_state=random_state)
        self.iterations = iterations
        self.learning_rate = learning_rate
        self.depth = depth
        self.kwargs = kwargs

    def fit(self, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray]) -> 'CatBoostWrapper':
        """Fit CatBoost model."""
        self._validate_input(X, y)

        logger.info(f"Fitting CatBoost on {X.shape[0]} samples...")
        start_time = time.time()

        try:
            from catboost import CatBoostClassifier, CatBoostRegressor

            if self.task_type == 'classification':
                self.model = CatBoostClassifier(
                    iterations=self.iterations,
                    learning_rate=self.learning_rate,
                    depth=self.depth,
                    random_state=self.random_state,
                    verbose=False,
                    **self.kwargs
                )
            else:
                self.model = CatBoostRegressor(
                    iterations=self.iterations,
                    learning_rate=self.learning_rate,
                    depth=self.depth,
                    random_state=self.random_state,
                    verbose=False,
                    **self.kwargs
                )

            self.model.fit(X, y)

            self.is_fitted = True
            self.fit_time = time.time() - start_time

            logger.info(f"CatBoost fitted in {self.fit_time:.2f} seconds")

        except ImportError:
            raise ImportError("Install CatBoost with: pip install catboost")
        except Exception as e:
            logger.error(f"Error fitting CatBoost: {e}")
            raise

        return self

    def predict(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Make predictions with CatBoost."""
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")

        self._validate_input(X)

        start_time = time.time()
        predictions = self.model.predict(X)
        self.predict_time = time.time() - start_time

        return predictions

    def _predict_proba_impl(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Predict class probabilities."""
        return self.model.predict_proba(X)

    def get_params(self, deep: bool = True) -> dict:
        """Get parameters."""
        params = super().get_params(deep)
        params.update({
            'iterations': self.iterations,
            'learning_rate': self.learning_rate,
            'depth': self.depth,
            **self.kwargs
        })
        return params


class LightGBMWrapper(BaseModelWrapper):
    """
    LightGBM wrapper.

    Parameters
    ----------
    task_type : str, default='classification'
        Task type: 'classification' or 'regression'
    n_estimators : int, default=100
        Number of boosting rounds
    learning_rate : float, default=0.1
        Step size shrinkage
    max_depth : int, default=-1
        Maximum tree depth (-1 for unlimited)
    random_state : int, default=42
        Random seed
    **kwargs : dict
        Additional LightGBM parameters
    """

    def __init__(
        self,
        task_type: str = 'classification',
        n_estimators: int = 100,
        learning_rate: float = 0.1,
        max_depth: int = -1,
        random_state: int = 42,
        **kwargs
    ):
        super().__init__(task_type=task_type, random_state=random_state)
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.max_depth = max_depth
        self.kwargs = kwargs

    def fit(self, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray]) -> 'LightGBMWrapper':
        """Fit LightGBM model."""
        self._validate_input(X, y)

        logger.info(f"Fitting LightGBM on {X.shape[0]} samples...")
        start_time = time.time()

        try:
            import lightgbm as lgb

            if self.task_type == 'classification':
                self.model = lgb.LGBMClassifier(
                    n_estimators=self.n_estimators,
                    learning_rate=self.learning_rate,
                    max_depth=self.max_depth,
                    random_state=self.random_state,
                    verbose=-1,
                    **self.kwargs
                )
            else:
                self.model = lgb.LGBMRegressor(
                    n_estimators=self.n_estimators,
                    learning_rate=self.learning_rate,
                    max_depth=self.max_depth,
                    random_state=self.random_state,
                    verbose=-1,
                    **self.kwargs
                )

            self.model.fit(X, y)

            self.is_fitted = True
            self.fit_time = time.time() - start_time

            logger.info(f"LightGBM fitted in {self.fit_time:.2f} seconds")

        except ImportError:
            raise ImportError("Install LightGBM with: pip install lightgbm")
        except Exception as e:
            logger.error(f"Error fitting LightGBM: {e}")
            raise

        return self

    def predict(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Make predictions with LightGBM."""
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")

        self._validate_input(X)

        start_time = time.time()
        predictions = self.model.predict(X)
        self.predict_time = time.time() - start_time

        return predictions

    def _predict_proba_impl(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """Predict class probabilities."""
        return self.model.predict_proba(X)

    def get_params(self, deep: bool = True) -> dict:
        """Get parameters."""
        params = super().get_params(deep)
        params.update({
            'n_estimators': self.n_estimators,
            'learning_rate': self.learning_rate,
            'max_depth': self.max_depth,
            **self.kwargs
        })
        return params
