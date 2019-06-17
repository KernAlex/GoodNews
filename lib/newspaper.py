import lib.article as article

# This thing is crap right now, there needs to be a hashset of strings
# that makes sure the articles are not repeated twice, etc.
class Page:

    def __init__(self):
        self.__articles = set()

    def add_article(self, article):
        assert isinstance(article, article.Article)
        self.__articles.add(article)

if __name__=="__main__":
    goog = article.Article("https://www.google.com")

