import logging
from logging.handlers import RotatingFileHandler

from decouple import config

logger = logging.getLogger("vpn_bot")
logger.setLevel(logging.INFO)

if logger.hasHandlers():
    logger.handlers.clear()

max_log_size = 500 * 1024 * 1024
backup_count = 2

file_handler = RotatingFileHandler(
    config("LOG_PATH"),
    maxBytes=max_log_size,
    backupCount=backup_count,
    encoding="utf-8",
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
