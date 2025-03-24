from logging.handlers import TimedRotatingFileHandler
import logging
import os
import config

logger = logging.getLogger(config.PROCESS_NAME)
logger.propagate = False


def get_logger(level=logging.INFO):
    logger.setLevel(level)
    if not logger.hasHandlers():
        logger.addHandler(logging.StreamHandler())
        log_path = get_path('logs', config.PROCESS_NAME + '.log')
        handler = TimedRotatingFileHandler(filename=log_path, when='D', interval=1)
        handler.setFormatter(logging.Formatter("%(asctime)s %(name)s [%(levelname)s][%(filename)s:%(lineno)d]: %(message)s"))
        logger.addHandler(handler)

    return logger


def get_path(directory, filename):
    generated_path = os.path.join(os.path.dirname(__name__), directory)
    if not os.path.exists(generated_path):
        os.makedirs(generated_path)

    return os.path.join(generated_path, filename)


def get_filepath(directory, file_name):
    return f"{directory}/{file_name}"
