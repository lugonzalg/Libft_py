import logging
from dataclasses import dataclass
import logging.config

import logging
import logging.config

@dataclass
class Logger(logging.Logger):


    _instance = None  # Initialize _instance at the class level

    def __new__(cls, name="simpleExample"):

        if cls._instance is None:
            logging.config.fileConfig('logging.conf')
            cls._instance = logging.getLogger(name)

        return cls._instance

    def __init__(self, name='mylogger', level=logging.NOTSET):
        super().__init__(name, level)

logger = Logger(name="paco")

logger1 = Logger()
logger1.info("This is a test message")

logger2 = Logger()
print(f"Logger1 is Logger2: {logger1 is logger2}")
