import os
import sys
from loguru import logger as LOGGER
from . import PATHS


app_log_level = os.getenv("LOGURU_LEVEL")
error_log_level = os.getenv("ERROR_LEVEL")
history_log_filename = os.path.join(PATHS.app_data_dir, os.getenv("HISTORY_LOG_FILENAME"))
history_log_level = os.getenv("HISTORY_LOG_LEVEL")
error_log_filename = os.path.join(PATHS.app_data_dir, os.getenv("ERROR_LOG_FILENAME"))
log_file_size = os.getenv("LOG_FILE_SIZE")
LOGGER.add(history_log_filename, level=history_log_level, rotation=log_file_size)
LOGGER.add(error_log_filename, level=error_log_level, rotation=log_file_size)
