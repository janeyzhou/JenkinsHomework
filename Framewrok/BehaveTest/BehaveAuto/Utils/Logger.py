# import logging
# import os
# import sys
#
# from pip._vendor.colorama import Fore
#
#
# class Logger:
#     def __init__(self):
#         self.logger = logging.getLogger()
#         log_level = logging.INFO
#         formatter = logging.Formatter(
#             '\n[%(levelname)s] [%(asctime)s] [%(threadName)s] [%(funcName)s] : %(message)s [%(filename)s:%(lineno)s]',
#             '%Y-%m-%d %H:%M:%S')
#         # console
#         console = logging.StreamHandler(stream=sys.stdout)
#         console.setLevel(log_level)
#         console.setFormatter(formatter)
#         self.logger.addHandler(console)
#         # console to file
#         # log_file = os.path.join(os.path.dirname(__file__), '..', '{}/behave_log.log'.format(path))
#         log_file = os.path.join(os.path.dirname(__file__), '..', 'Report/behave_log.log')
#         file_console = logging.FileHandler(log_file, mode='w')
#         file_console.setLevel(log_level)
#         file_console.setFormatter(formatter)
#
#     def info(self, message):
#         self.logger.info(message)
#
#     def debug(self, message):
#         self.logger.debug(message)
#
#     def warning(self, message):
#         colored_msg = Fore.YELLOW + str(message) + Fore.RESET
#         self.logger.warning(colored_msg)
#
#     def error(self, message):
#         colored_msg = Fore.RED + str(message) + Fore.RESET
#         self.logger.error(colored_msg)
#
#
# logger = Logger()

import logging
import os


def init_logging(path):
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
    log_file = os.path.join(os.path.dirname(__file__), '..', '{}/behave_log.log'.format(path))
    file_console = logging.FileHandler(log_file, mode="w")
    file_console.setLevel(log_level)
    file_console.setFormatter(formatter)
    # Add the handler to the root logger
    logger.addHandler(file_console)
    logger.addHandler(console)
