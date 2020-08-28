import json

class ReadTestData:
    def __init__(self):
        pass

    @staticmethod
    def read_test_data(file_path):
        with open(file=file_path ) as f:
            data = json.load(f)
        return data

