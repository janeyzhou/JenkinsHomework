import requests


class Rest:
    def __init__(self):
        pass

    def get_request(self, url):
        print("Johnson")
        return requests.get(url)

    def post_request(self, url, data):
        return requests.post(url, data=data)