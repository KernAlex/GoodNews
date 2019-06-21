import requests
import lib.general_funcitions as funcs
debug = True


# Some skeleton code for the article class
class Article:
    def __init__(self, url):
        self.url = url
        self.story = funcs.extract_sentences(requests.get(url).text)

    def __hash__(self):
        """
        :return: url is the hash in articles, using a "String" hash
        >>> A1 = Article("https://www.alexkern.dev")
        >>> A2 = Article("https://www.alexkern.com")
        >>> articles = {A1, A2}
        >>> print(len(articles))
        2
        >>> A3 = Article("https://www.alexkern.dev")
        >>> articles.add(A3)
        >>> print(len(articles))
        2
        """
        return hash(self.url)

    def __eq__(self, other):
        # another object is equal to self, iff
        # it is an instance of Article and the urls are equal
        return isinstance(other, Article) and self.url == other.url
if debug:
    import doctest
    doctest.testmod()

if __name__=="__main__":
    x = 2