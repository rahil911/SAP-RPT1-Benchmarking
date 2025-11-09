"""
SAP RPT-1 Benchmarking Package Setup
=====================================

Author: UW MSIM Team
Date: November 2025
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sap-rpt1-benchmarking",
    version="1.0.0",
    author="UW MSIM Team",
    author_email="rahilharihar@uw.edu",
    description="Comprehensive benchmarking suite for SAP RPT-1 and tabular ML models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/[your-repo]/sap-rpt1-benchmarking",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=1.0.0",
        "scipy>=1.7.0",
        "pyyaml>=6.0",
        "tqdm>=4.62.0",
        "openml>=0.12.0",
        "psutil>=5.8.0",
        "gputil>=1.4.0"
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0",
            "black>=21.6b0",
            "flake8>=3.9.0",
            "mypy>=0.910"
        ],
        "models": [
            "xgboost>=1.5.0",
            "catboost>=1.0.0",
            "lightgbm>=3.3.0",
            "autogluon.tabular>=0.5.0",
            "tabpfn>=0.1.0"
        ],
        "analysis": [
            "matplotlib>=3.4.0",
            "seaborn>=0.11.0",
            "scikit-posthocs>=0.7.0"
        ]
    },
)
