import os
import sys
from loguru import logger as LOGGER


app_log_level = os.getenv("LOGURU_LEVEL") or "DEBUG"
LOGGER.remove()
LOGGER.add(sys.stderr, level=app_log_level)

