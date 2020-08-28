import logging
import sys

from colorama import Fore


class Logger:

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s', '%Y-%m-%d %H:%M:%S')
        console = logging.StreamHandler(stream=sys.stdout)
        console.setFormatter(formatter)
        self.logger.addHandler(console)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        colored_msg = Fore.YELLOW + str(message) + Fore.RESET
        self.logger.warning(colored_msg)

    def error(self, message):
        colored_msg = Fore.RED + str(message) + Fore.RESET
        self.logger.error(colored_msg)


logger = Logger()
