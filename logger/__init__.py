import sys

from loguru import logger

from config import LogConfig

logger.remove(0)

logger.add(sys.stdout, serialize=LogConfig.structured, level=LogConfig.level)
