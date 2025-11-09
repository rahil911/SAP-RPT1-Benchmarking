"""
SAP RPT-1 Wrapper
=================

Sklearn-compatible wrapper for SAP RPT-1-OSS.

SAP RPT-1 uses in-context learning with pretrained transformers.
Requires Python 3.11 and Hugging Face model access.

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


class SAPRPT1Wrapper(BaseModelWrapper):
    """
    SAP RPT-1 (Retrieval Pretrained Transformer) wrapper.

    Parameters
    ----------
    task_type : str, default='classification'
        Task type: 'classification' or 'regression'
    context_size : int, default=4096
        Maximum context window size in tokens
    bagging_factor : int, default=4
        Number of bagging iterations for prediction stability
    model_size : str, default='small'
        Model size: 'small' or 'large'
    device : str, default='auto'
        Device to use: 'cpu', 'cuda', or 'auto'
    random_state : int, default=42
        Random seed for reproducibility
    """

    def __init__(
        self,
        task_type: str = 'classification',
        context_size: int = 4096,
        bagging_factor: int = 4,
        model_size: str = 'small',
        device: str = 'auto',
        random_state: int = 42
    ):
        super().__init__(task_type=task_type, random_state=random_state)
        self.context_size = context_size
        self.bagging_factor = bagging_factor
        self.model_size = model_size
        self.device = device

    def fit(self, X: Union[pd.DataFrame, np.ndarray], y: Union[pd.Series, np.ndarray]) -> 'SAPRPT1Wrapper':
        """
        Train SAP RPT-1 model.

        Note: SAP RPT-1 uses in-context learning, so "training" is primarily
        about storing the training data for retrieval during inference.

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Training features
        y : pd.Series or np.ndarray, shape (n_samples,)
            Training target

        Returns
        -------
        self : SAPRPT1Wrapper
            Fitted model
        """
        self._validate_input(X, y)

        logger.info(f"Fitting SAP RPT-1 ({self.model_size}) on {X.shape[0]} samples...")
        start_time = time.time()

        try:
            # Import here to avoid import errors in environments without SAP RPT-1
            from sap_rpt_1_oss import SAP_RPT_OSS_Classifier, SAP_RPT_OSS_Regressor

            # Initialize appropriate model
            if self.task_type == 'classification':
                self.model = SAP_RPT_OSS_Classifier(
                    context_size=self.context_size,
                    bagging_factor=self.bagging_factor,
                    model_size=self.model_size,
                    device=self.device
                )
            else:
                self.model = SAP_RPT_OSS_Regressor(
                    context_size=self.context_size,
                    bagging_factor=self.bagging_factor,
                    model_size=self.model_size,
                    device=self.device
                )

            # Fit model (stores training data for in-context learning)
            self.model.fit(X, y)

            self.is_fitted = True
            self.fit_time = time.time() - start_time

            logger.info(f"SAP RPT-1 fitted in {self.fit_time:.2f} seconds")

        except ImportError as e:
            logger.error(f"SAP RPT-1 not installed: {e}")
            raise ImportError(
                "SAP RPT-1 not found. Install with: "
                "pip install git+https://github.com/SAP-samples/sap-rpt-1-oss.git"
            )
        except Exception as e:
            logger.error(f"Error fitting SAP RPT-1: {e}")
            raise

        return self

    def predict(self, X: Union[pd.DataFrame, np.ndarray]) -> np.ndarray:
        """
        Make predictions with SAP RPT-1.

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

        logger.info(f"Predicting on {X.shape[0]} samples with SAP RPT-1...")
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
        Implementation of predict_proba for SAP RPT-1.

        Parameters
        ----------
        X : pd.DataFrame or np.ndarray, shape (n_samples, n_features)
            Test features

        Returns
        -------
        probabilities : np.ndarray, shape (n_samples, n_classes)
            Class probabilities
        """
        if self.task_type != 'classification':
            raise ValueError("predict_proba only available for classification")

        try:
            return self.model.predict_proba(X)
        except AttributeError:
            # Fallback if predict_proba not available
            logger.warning("predict_proba not available, using one-hot encoding of predictions")
            predictions = self.model.predict(X)
            n_samples = len(predictions)
            n_classes = len(np.unique(predictions))
            proba = np.zeros((n_samples, n_classes))
            proba[np.arange(n_samples), predictions] = 1.0
            return proba

    def get_params(self, deep: bool = True) -> dict:
        """Get parameters for this estimator."""
        params = super().get_params(deep)
        params.update({
            'context_size': self.context_size,
            'bagging_factor': self.bagging_factor,
            'model_size': self.model_size,
            'device': self.device
        })
        return params
