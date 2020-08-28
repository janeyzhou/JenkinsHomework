class ReadConfig:
    def __init__(self, env):
        self.env = env

    def read_config(self, file_path):
        with open(file= file_path) as f:
            f.read()