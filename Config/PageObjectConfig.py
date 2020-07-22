import os

from Util.BaseConfig import BaseConfig


class PageObjectConfig(BaseConfig):

    def __init__(self):
        page_object_config_path = os.path.join(os.path.dirname(__file__), "cfg.ini")
        super().__init__(page_object_config_path)

        self.Domain = self.get("Default", "ChromeDriver")


cfg = PageObjectConfig()

