import logging
import os


def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    level = os.environ.get("LOG_LEVEL") or logging.DEBUG
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger


if __name__ == "__main__":
    get_module_logger(__name__).info("Logging test!")
