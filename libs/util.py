from loguru import logger

class Loggings:
    def __init__(self, log_file):
        logger.add(f"{log_file}", level="INFO", encoding="utf-8", enqueue=True)

    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)