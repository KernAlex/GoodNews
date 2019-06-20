import requests
import lib.general_funcitions as funcs


# Some skeleton code for the article class
class Article:
    def __init__(self, url):
        self.url = url
        self.story = funcs.extract_sentences(requests.get(url).text)

    def __hash__(self):
        return hash(self.url)

    def __eq__(self, other):
        # another object is equal to self, iff
        # it is an instance of Article and the urls are equal
        return isinstance(other, Article) and self.url == other.url
