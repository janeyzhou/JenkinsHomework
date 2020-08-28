import logging


def init_logging():
    # Init the root logger object
    logger = logging.getLogger('')
    log_level = logging.INFO
    # log_level = logging.DEBUG
    # log_level = logging.ERROR
    log_style = "[%(levelname)s]--[%(asctime)s]--[%(threadName)s]--[%(funcName)-12s]: %(message)s (%(filename)s:%(lineno)s)\n"
    # Set a format which is simpler for console use
    formatter = logging.Formatter(log_style, "%Y-%m-%d %H:%M:%S")
    # console
    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(formatter)
    # file_console
    file_console = logging.FileHandler('example.log', mode="w")
    file_console.setLevel(log_level)
    file_console.setFormatter(formatter)
    # Add the handler to the root logger
    logger.addHandler(file_console)
    logger.addHandler(console)
