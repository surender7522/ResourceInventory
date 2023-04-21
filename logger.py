import logging
import os
from logging.handlers import RotatingFileHandler

from env import LOGGING_LEVEL

max_log_file_size = 5242880
logger_name = "ri_logger"
files_count = 5
logger = logging.getLogger("ri-log")
logfiledir = os.path.dirname(os.path.abspath(__file__)) + "/logs"
logfilepath = logfiledir + "/ri.log"


def initialize():
    global logger
    # logging.Formatter('{asctime} - {name} - {levelname:8s} - {message}', style ='{')
    formatter = logging.Formatter(
        "[%(asctime)s] - {%(filename)s:%(funcName)s:%(lineno)d} - %(levelname)s - %(message)s"
    )
    if not os.path.exists(logfiledir):
        try:
            os.makedirs(logfiledir)
        except FileExistsError:
            pass
    logger = logging.getLogger("ri-log")
    if LOGGING_LEVEL == "debug":
        logger.setLevel(logging.DEBUG)
    elif LOGGING_LEVEL == "info":
        logger.setLevel(logging.INFO)
    elif LOGGING_LEVEL == "warning":
        logger.setLevel(logging.WARNING)
    elif LOGGING_LEVEL == "error":
        logger.setLevel(logging.ERROR)
    elif LOGGING_LEVEL == "critical":
        logger.setLevel(logging.CRITICAL)

    # add a rotating handler
    handler = RotatingFileHandler(
        logfilepath, maxBytes=max_log_file_size, backupCount=files_count - 1
    )
    handler.setLevel("DEBUG")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel("DEBUG")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


def savelog(action, message):
    if action == "debug":
        logger.debug(message)
    elif action == "info":
        logger.info(message)
    elif action == "warning":
        logger.warning(message)
    elif action == "error":
        logger.error(message)
    elif action == "critical":
        logger.critical(message)
    else:
        print("fdfdfdfdfd")
    return
