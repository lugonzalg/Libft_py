import logging
import os

from dataclasses import dataclass

class Logger:

    name: str
    path: str

    def set_logger(self) -> None:
        logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO").upper(),
                            format="%(asctime)s - %(levelname)s - %(name)s -  %(message)s",
                            datefmt="%m/%d/%Y %H:%M:%S",
                            filename=path + name + ".log",
                            filemode='w')

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(name)s -  %(message)s"))
        logging.getLogger(name).addHandler(console)
        self.logger = logging.getLogger(name)
