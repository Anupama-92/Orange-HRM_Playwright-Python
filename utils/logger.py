# utilities/logger.py
import logging
import os
from datetime import datetime


def get_logger(name: str):
    """Configure and return a logger for tests"""
    # Create logs folder if not exists
    os.makedirs("logs", exist_ok=True)

    log_filename = datetime.now().strftime("logs/test_log_%Y-%m-%d.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent adding duplicate handlers
    if not logger.handlers:
        # File Handler
        fh = logging.FileHandler(log_filename, mode="a", encoding="utf-8")
        fh.setLevel(logging.DEBUG)

        # Console Handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
