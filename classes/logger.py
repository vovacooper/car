__author__ = 'vovacooper'

import logging
import os

level = logging.DEBUG

if not os.path.exists("/var/www/car/log/"):
    os.makedirs("/var/www/car/log/")

logger = logging.getLogger("logger")
logger.setLevel(level)

fh = logging.FileHandler("/var/www/car/log/care_log.log")
fh.setLevel(level)

formatter = logging.Formatter("%(asctime)s %(module)s.%(funcName)s -> %(lineno)d-%(levelname)s: %(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)

########################################################################################################################
if __name__ == "__main__":
   logger.warning("log log log log log log")
