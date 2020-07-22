import logging
import sys

from colorama import Fore


class Logger:
    def __init__(self):
        self.logger = logging.getLogger()

        log_level = logging.INFO
        log_formatter = logging.Formatter('[%(levelname)s] [%(asctime)s]: %(message)s',
                                          "%Y-%m-%d %H:%M:%S")
        console = logging.StreamHandler(stream=sys.stdout)
        console.setLevel(log_level)
        console.setFormatter(log_formatter)
        self.logger.addHandler(console)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        colored_msg = Fore.RED + str(message) + Fore.RESET
        self.logger.error(colored_msg)

logger = Logger()

# def init_logger():
#     logger = logging.getLogger()
#     log_level = logging.INFO
#     log_formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] [(%(filename)s:%(lineno)s)] : %(message)s',
#                                       "%Y-%m-%d %H:%M:%S")
#
#     console = logging.StreamHandler()
#     console.setLevel(log_level)
#     console.setFormatter(log_formatter)
#     logger.addHandler(console)






