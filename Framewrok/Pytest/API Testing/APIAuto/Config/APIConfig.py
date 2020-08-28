import os

from APIAuto.Utils.BaseConfig import BaseConfig


class AIPConfig:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'cfg.ini')
    config = BaseConfig(file_path)

    def __init__(self):
        self.domain = self.config.get('DEV', 'DEV_DOMAIN') if self.config.get("DEFAULT", "LOCAL") else self.config.get(
            'QA', 'QA_DOMAIN')
        self.Employee_Test_Data_Path = self.config.get("DEFAULT", "Employee_Test_Data_Path")


cfg = AIPConfig()
