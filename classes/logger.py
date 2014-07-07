__author__ = 'vovacooper'

import logging
import os

level = logging.DEBUG


if not os.path.exists("/var/log/flask-uwsgi/"):
    os.makedirs("/var/log/flask-uwsgi/")

logger = logging.getLogger("logger")
logger.setLevel(level)

fh = logging.FileHandler("/var/log/flask-uwsgi/car_log.log")
fh.setLevel(level)

formatter = logging.Formatter("%(asctime)s %(module)s.%(funcName)s -> %(lineno)d-%(levelname)s: %(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)

########################################################################################################################
if __name__ == "__main__":
    logger.info("Starting ")
    logger.warning("log log log log log log")
