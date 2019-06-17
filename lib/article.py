import requests

class Article:
    def __init__(self, url):
        self.art = requests.get(url)