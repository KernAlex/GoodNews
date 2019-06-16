from lib.article import Article


########################################
#
# This is only an example, design before
# implementation, do not worry about
# optimization.
#
########################################



if __name__=="__main__":
    # as an aside, in the end this specific article should give a very bad rating when parsed
    PVTL = Article("http://www.baystreet.ca/articles/techinsider.aspx?articleid=48609")
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(PVTL.art.text)
    s = str(soup)
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(s)

    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')