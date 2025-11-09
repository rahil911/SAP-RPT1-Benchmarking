"""
TabPFN Wrapper
==============

Sklearn-compatible wrapper for TabPFN (Tabular Pre-trained Transformers).

TabPFN is a pretrained model for tabular classification using
in-context learning (no training required).

Author: UW MSIM Team
Date: November 2025
"""

import time
import logging
from typing import Optional, Union
import numpy as np
import pandas as pd

from .base_wrapper import BaseModelWrapper

logger = logging.getLogger(__name__)


class TabPFNWrapper(BaseModelWrapper):
    """
    TabPFN (Tabular Prior-Fitted Networks) wrapper.

    TabPFN uses pretrained transformers for zero-shot tabular prediction.
    Works best on datasets with <1000 samples and <100 features.

    Parameters
    ----------
    task_type : str, default='classification'
        Task type (only 'classification' supported by TabPFN)
    n_ensemble : int, default=1
        Number of ensemble members
    device : str, default='auto'
        Device: 'cpu', 'cuda', or 'auto'
    random_state : int, default=42
        Random seed
    """

    def __init__(
        self,
        task_type: str = 'classification',
        n_ensemble: int = 1,
        device: str = 'auto',
        random_state: int = 42
    ):
        super().__init__(task_type=task_type, random_state=random_state)

        if task_type != 'classification':
            raise ValueError("TabPFN only supports classification tasks")

        self.n_ensemble = n_ensemble
        self.device = device

    def fit(self, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray]) -> 'TabPFNWrapper':
        """
        Fit TabPFN (stores training data for in-context learning).

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Training features (max 1000 samples, 100 features)
        y : pd.Series or np.ndarray, shape (n_samples,)
            Training target

        Returns
        -------
        self : TabPFNWrapper
            Fitted model
        """
        self._validate_input(X, y)

        # Check TabPFN constraints
        if X.shape[0] > 1000:
            logger.warning(f"TabPFN works best with <1000 samples, got {X.shape[0]}")

        if X.shape[1] > 100:
            logger.warning(f"TabPFN works best with <100 features, got {X.shape[1]}")

        logger.info(f"Fitting TabPFN on {X.shape[0]} samples...")
        start_time = time.time()

        try:
            from tabpfn import TabPFNClassifier

            self.model = TabPFNClassifier(
                device=self.device,
                N_ensemble_configurations=self.n_ensemble
            )

            # Fit model
            self.model.fit(X, y)

            self.is_fitted = True
            self.fit_time = time.time() - start_time

            logger.info(f"TabPFN fitted in {self.fit_time:.2f} seconds")

        except ImportError:
            logger.error("TabPFN not installed")
            raise ImportError("Install TabPFN with: pip install tabpfn")
        except Exception as e:
            logger.error(f"Error fitting TabPFN: {e}")
            raise

        return self

    def predict(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """
        Make predictions with TabPFN.

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Test features

        Returns
        -------
        predictions : np.ndarray, shape (n_samples,)
            Predicted class labels
        """
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")

        self._validate_input(X)

        logger.info(f"Predicting on {X.shape[0]} samples with TabPFN...")
        start_time = time.time()

        try:
            predictions = self.model.predict(X)
            self.predict_time = time.time() - start_time

            logger.info(f"Predictions complete in {self.predict_time:.2f} seconds")

            return predictions

        except Exception as e:
            logger.error(f"Error during prediction: {e}")
            raise

    def _predict_proba_impl(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """
        Predict class probabilities with TabPFN.

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Test features

        Returns
        -------
        probabilities : np.ndarray, shape (n_samples, n_classes)
            Class probabilities
        """
        return self.model.predict_proba(X)

    def get_params(self, deep: bool = True) -> dict:
        """Get parameters for this estimator."""
        params = super().get_params(deep)
        params.update({
            'n_ensemble': self.n_ensemble,
            'device': self.device
        })
        return params
