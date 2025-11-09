"""
Data Preprocessing Utilities
=============================

Minimal preprocessing for tabular datasets.

Handles:
- Missing value imputation
- Categorical encoding
- Feature scaling
- Train/test splitting

Author: UW MSIM Team
Date: November 2025
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from typing import Tuple, Optional, List
import logging

logger = logging.getLogger(__name__)


class TabularPreprocessor:
    """
    Minimal preprocessing pipeline for tabular data.

    Parameters
    ----------
    handle_missing : str, default='mean'
        Strategy for missing values: 'mean', 'median', 'most_frequent', 'drop'
    encode_categoricals : bool, default=True
        Whether to encode categorical features
    scale_features : bool, default=False
        Whether to standardize numerical features
    """

    def __init__(
        self,
        handle_missing: str = 'mean',
        encode_categoricals: bool = True,
        scale_features: bool = False
    ):
        self.handle_missing = handle_missing
        self.encode_categoricals = encode_categoricals
        self.scale_features = scale_features

        self.numerical_imputer = None
        self.categorical_imputer = None
        self.scaler = None
        self.label_encoders = {}
        self.categorical_columns = []
        self.numerical_columns = []

    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None):
        """
        Fit preprocessor on training data.

        Parameters
        ----------
        X : pd.DataFrame
            Training features
        y : pd.Series, optional
            Training target (not used, for sklearn compatibility)
        """
        # Identify column types
        self.categorical_columns = X.select_dtypes(include=['object', 'category']).columns.tolist()
        self.numerical_columns = X.select_dtypes(include=[np.number]).columns.tolist()

        logger.info(f"Preprocessing: {len(self.numerical_columns)} numerical, {len(self.categorical_columns)} categorical features")

        # Fit numerical imputer
        if self.numerical_columns and self.handle_missing != 'drop':
            strategy = self.handle_missing if self.handle_missing in ['mean', 'median', 'most_frequent'] else 'mean'
            self.numerical_imputer = SimpleImputer(strategy=strategy)
            self.numerical_imputer.fit(X[self.numerical_columns])

        # Fit categorical imputer
        if self.categorical_columns and self.handle_missing != 'drop':
            self.categorical_imputer = SimpleImputer(strategy='most_frequent')
            self.categorical_imputer.fit(X[self.categorical_columns])

        # Fit label encoders
        if self.encode_categoricals and self.categorical_columns:
            for col in self.categorical_columns:
                le = LabelEncoder()
                # Handle missing values before encoding
                non_null_values = X[col].dropna()
                if len(non_null_values) > 0:
                    le.fit(non_null_values)
                    self.label_encoders[col] = le

        # Fit scaler
        if self.scale_features and self.numerical_columns:
            self.scaler = StandardScaler()
            X_num_imputed = self.numerical_imputer.transform(X[self.numerical_columns]) if self.numerical_imputer else X[self.numerical_columns]
            self.scaler.fit(X_num_imputed)

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Transform data using fitted preprocessor.

        Parameters
        ----------
        X : pd.DataFrame
            Features to transform

        Returns
        -------
        X_transformed : pd.DataFrame
            Transformed features
        """
        X = X.copy()

        # Handle numerical features
        if self.numerical_columns:
            if self.handle_missing == 'drop':
                X = X.dropna(subset=self.numerical_columns)
            elif self.numerical_imputer:
                X[self.numerical_columns] = self.numerical_imputer.transform(X[self.numerical_columns])

            # Scale if needed
            if self.scale_features and self.scaler:
                X[self.numerical_columns] = self.scaler.transform(X[self.numerical_columns])

        # Handle categorical features
        if self.categorical_columns:
            if self.handle_missing == 'drop':
                X = X.dropna(subset=self.categorical_columns)
            elif self.categorical_imputer:
                X[self.categorical_columns] = self.categorical_imputer.transform(X[self.categorical_columns])

            # Encode categoricals
            if self.encode_categoricals:
                for col in self.categorical_columns:
                    if col in self.label_encoders:
                        le = self.label_encoders[col]
                        # Handle unseen categories
                        X[col] = X[col].apply(
                            lambda x: le.transform([x])[0] if x in le.classes_ else -1
                        )

        return X

    def fit_transform(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> pd.DataFrame:
        """Fit and transform in one step."""
        return self.fit(X, y).transform(X)


def load_dataset(
    dataset_path: str,
    target_col: str = 'target'
) -> Tuple[pd.DataFrame, pd.Series, str]:
    """
    Load a dataset from CSV files.

    Parameters
    ----------
    dataset_path : str
        Path to dataset directory or base filename
    target_col : str
        Name of target column

    Returns
    -------
    X : pd.DataFrame
        Features
    y : pd.Series
        Target
    task_type : str
        'classification' or 'regression'
    """
    # Try loading X and y separately
    if os.path.isdir(dataset_path):
        # Find X and y files
        files = os.listdir(dataset_path)
        X_file = [f for f in files if f.endswith('_X.csv')][0]
        y_file = [f for f in files if f.endswith('_y.csv')][0]

        X = pd.read_csv(os.path.join(dataset_path, X_file))
        y = pd.read_csv(os.path.join(dataset_path, y_file)).iloc[:, 0]
    else:
        # Load combined file
        data = pd.read_csv(dataset_path)
        y = data[target_col]
        X = data.drop(columns=[target_col])

    # Determine task type
    if y.dtype == 'object' or len(y.unique()) < 20:
        task_type = 'classification'
    else:
        task_type = 'regression'

    logger.info(f"Loaded dataset: {X.shape[0]} samples, {X.shape[1]} features, task={task_type}")

    return X, y, task_type
