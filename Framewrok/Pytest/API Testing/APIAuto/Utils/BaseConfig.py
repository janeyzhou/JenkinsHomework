import configparser
from configparser import ExtendedInterpolation


class BaseConfig:

    def __init__(self, filename):
        self.config_data = configparser.ConfigParser()
        self.config_data.read(filename)

    def get(self, section_name, key):
        return self.config_data.get(section_name, key)
