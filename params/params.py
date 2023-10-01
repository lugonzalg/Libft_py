from .Logger import logger
import yaml
import sys
import os

PARAMS = os.environ["PARAMS"]

try:
    with open(PARAMS, 'r') as config_file:
        config_data = yaml.safe_load(config_file)
except FileNotFoundError as file_error:
    logger.logger.error(f"Error: {file_error}")
    sys.exit(1)