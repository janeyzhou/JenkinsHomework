from configparser import ConfigParser, ExtendedInterpolation


class BaseConfig:
    def __init__(self, file_path):
        self.config_content = ConfigParser(allow_no_value=True, interpolation=ExtendedInterpolation())
        self.config_content.read(file_path)

    def get(self, section, key):
        return self.config_content.get(section, key)


