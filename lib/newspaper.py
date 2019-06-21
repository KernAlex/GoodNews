import lib.article as article

# A collection or articles.
# for each domain in Page there will be a map pointing to the list of articles,
# as well as a set of articles in the domin. This means that
class Page:

    def __init__(self):
        self.__articles = {}

    def add_article(self, url, depth):
        """
        :param url: the article to add
        :param depth: how deep does the depth first search reach before stopping
        :return: None
        """

        pass

    def get_sections(self):
        """
        :return: list of domains in articles
        """
        return self.__articles.keys()

    def get_articles(self, domain_key):
        """
        :param domain_key: a key of the articles in the form http://www.somepage.com
        :return: set of articles
        """
        assert domain_key in self.__articles, 'Domain does not exist in this Page'
        pass


if __name__=="__main__":
    goog = article.Article("https://www.google.com")

