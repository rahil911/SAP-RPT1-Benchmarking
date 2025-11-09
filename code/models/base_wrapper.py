"""
Base Model Wrapper
==================

Abstract base class for all model wrappers.
Ensures sklearn-compatible interface for consistent evaluation.

Author: UW MSIM Team
Date: November 2025
"""

from abc import ABC, abstractmethod
from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin
import time
import logging
from typing import Any, Optional
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class BaseModelWrapper(BaseEstimator, ABC):
    """
    Base class for all model wrappers.

    Ensures sklearn-compatible interface with:
    - fit(X, y): Train the model
    - predict(X): Make predictions
    - predict_proba(X): Predict class probabilities (classification only)

    Also tracks timing information:
    - fit_time: Time spent in training
    - predict_time: Time spent in prediction

    Parameters
    ----------
    task_type : str, default='classification'
        Type of task: 'classification' or 'regression'
    random_state : int, optional
        Random seed for reproducibility
    """

    def __init__(
        self,
        task_type: str = 'classification',
        random_state: Optional[int] = 42
    ):
        self.task_type = task_type
        self.random_state = random_state
        self.model = None
        self.fit_time: Optional[float] = None
        self.predict_time: Optional[float] = None
        self.is_fitted: bool = False

    @abstractmethod
    def fit(self, X: Any, y: Any) -> 'BaseModelWrapper':
        """
        Train the model on provided data.

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Training features
        y : pd.Series or np.ndarray, shape (n_samples,)
            Training target

        Returns
        -------
        self : BaseModelWrapper
            Returns self for method chaining
        """
        pass

    @abstractmethod
    def predict(self, X: Any) -> np.ndarray:
        """
        Make predictions on new data.

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Test features

        Returns
        -------
        predictions : np.ndarray, shape (n_samples,)
            Predicted values or class labels
        """
        pass

    def predict_proba(self, X: Any) -> np.ndarray:
        """
        Predict class probabilities (classification only).

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Test features

        Returns
        -------
        probabilities : np.ndarray, shape (n_samples, n_classes)
            Class probabilities

        Raises
        ------
        NotImplementedError
            If task_type is not 'classification'
        ValueError
            If model is not fitted
        """
        if self.task_type != 'classification':
            raise NotImplementedError(
                f"predict_proba only available for classification tasks, "
                f"got task_type='{self.task_type}'"
            )

        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")

        start_time = time.time()
        proba = self._predict_proba_impl(X)
        self.predict_time = time.time() - start_time

        return proba

    @abstractmethod
    def _predict_proba_impl(self, X: Any) -> np.ndarray:
        """
        Implementation of predict_proba (model-specific).

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Test features

        Returns
        -------
        probabilities : np.ndarray, shape (n_samples, n_classes)
            Class probabilities
        """
        pass

    def get_params(self, deep: bool = True) -> dict:
        """
        Get parameters for this estimator (sklearn compatibility).

        Parameters
        ----------
        deep : bool, default=True
            If True, return parameters for sub-estimators

        Returns
        -------
        params : dict
            Parameter names mapped to their values
        """
        return {
            'task_type': self.task_type,
            'random_state': self.random_state
        }

    def set_params(self, **params) -> 'BaseModelWrapper':
        """
        Set parameters for this estimator (sklearn compatibility).

        Parameters
        ----------
        **params : dict
            Estimator parameters

        Returns
        -------
        self : BaseModelWrapper
            Returns self
        """
        for key, value in params.items():
            setattr(self, key, value)
        return self

    def _validate_input(self, X: Any, y: Optional[Any] = None):
        """
        Validate input data format.

        Parameters
        ----------
        X : any
            Features
        y : any, optional
            Target (if provided)
        """
        # Convert to pandas if needed
        if not isinstance(X, (pd.DataFrame, np.ndarray)):
            raise TypeError(
                f"X must be pd.DataFrame or np.ndarray, got {type(X)}"
            )

        if y is not None and not isinstance(y, (pd.Series, np.ndarray)):
            raise TypeError(
                f"y must be pd.Series or np.ndarray, got {type(y)}"
            )

    def __repr__(self) -> str:
        """String representation of the model."""
        params = self.get_params()
        param_str = ', '.join(f"{k}={v}" for k, v in params.items())
        return f"{self.__class__.__name__}({param_str})"
