# -*- coding: utf-8 -*-
import logging
import os.path
import sys
from logging.handlers import RotatingFileHandler
from typing import Dict

from settings import LOGS_DIR

os.makedirs(LOGS_DIR, exist_ok=True)


# Set max log file size to 1MB
MAX_LOG_FILE_SIZE_BYTES = 1000000  # 1MB

_loggers: Dict[str, logging.Logger] = {}


def get_logger(
    log_name: str, stdout_level: int = logging.INFO, file_level: int = logging.DEBUG
) -> logging.Logger:
    """
    Get a logger for the given name
    :param log_name: The name of the logger
    :param stdout_level: The level of logging to stdout
    :param file_level: The level of logging to the file
    :return: The logger
    """
    if log_name in _loggers:
        return _loggers[log_name]

    log_file = RotatingFileHandler(
        filename=os.path.join(LOGS_DIR, f"{log_name}.log"),
        encoding="utf-8",
        mode="a+",
        maxBytes=MAX_LOG_FILE_SIZE_BYTES,
        backupCount=5,
    )

    log_file.setFormatter(
        logging.Formatter("%(asctime)s %(name)-8s %(levelname)-8s %(message)s")
    )
    log_file.setLevel(file_level)

    log_stdout = logging.StreamHandler(sys.stdout)
    log_stdout.setFormatter(
        logging.Formatter("%(asctime)s %(name)-8s %(levelname)-8s %(message)s")
    )
    log_stdout.setLevel(stdout_level)

    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    logger.addHandler(log_file)
    logger.addHandler(log_stdout)

    _loggers[log_name] = logger
    return logger
