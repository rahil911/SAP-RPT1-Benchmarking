"""
Logging Utilities
=================

Structured logging for experiments.

Author: UW MSIM Team
Date: November 2025
"""

import logging
import sys
from pathlib import Path


def setup_logger(
    name: str,
    log_file: str = None,
    level: int = logging.INFO,
    format_string: str = None
) -> logging.Logger:
    """
    Setup logger with file and console handlers.

    Parameters
    ----------
    name : str
        Logger name
    log_file : str, optional
        Log file path
    level : int
        Logging level
    format_string : str, optional
        Custom format string

    Returns
    -------
    logger : logging.Logger
        Configured logger
    """
    if format_string is None:
        format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers = []  # Clear existing handlers

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter(format_string))
    logger.addHandler(console_handler)

    # File handler (if specified)
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(logging.Formatter(format_string))
        logger.addHandler(file_handler)

    return logger
