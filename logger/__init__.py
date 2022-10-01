import sys

from loguru import logger

# TODO: JSON logging in production only - or configured via .env that is

logger.add(sys.stdout, serialize=True)
