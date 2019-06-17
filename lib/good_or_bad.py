import doctest
debug = True
# Added samples for testing. F
# bad: http://www.baystreet.ca/articles/techinsider.aspx?articleid=48609
# good: https://www.zacks.com/stock/news/413724/twist-bioscience-twst-catches-eye-stock-jumps-8?cid=CS-MKTWTCH-HL-413724
# neutral: https://globalnews.ca/news/3393970/first-look-at-gender-neutral-washrooms-at-sacred-heart-community-school/
if debug:
    sample_bad_article = "Markets are now realizing the rapid growth in Software-as-a-Service (or ‘SaaS’) companies " \
                     "is over. Pivotal (NYSE:PVTL) and Cloudera (NYSE:CLDR) both spooked investors after reporting " \
                     "very weak results and fell 45.6% and 44%, respectively. What happened? Cloudera’s CEO resigned " \
                     "just as the company reported weak first quarter revenues of $187.5M, up 81% Y/Y. It lost " \
                     "$0.38 a share. For Q2, its revenue of $180-$183 million is below the $203.2 consensus. FY20 " \
                     "revenue will come in even worse than expected: $745 million - $765 million, compared to the " \
                     "$843.8 million consensus. Cloudera blamed its merger created uncertainties for customers but " \
                     "management clearly did not transition the business to plan for product enhancements in the " \
                     "pipeline. At this pace of revenue growth deceleration and mounting losses, investors should " \
                     "avoid Cloudera stock. Pivotal cut its full-year revenue to $756M - $767M, down from its " \
                     "previous guidance of $798M - $806M. With the stock price below $11, the stock trades at a " \
                     "price/sales of four times, half of where it was prior to the drop. Still, at a 15% revenue " \
                     "growth rate, the Enterprise platform market is shrinking. Customers may choose Amazon, Google, " \
                         "or Microsoft platforms instead, much to the detriment of Pivotal’s business. "
    sample_good_article = "Twist Bioscience Corporation (TWST - Free Report)	was a big mover last session, as the " \
                          "company saw its shares rise nearly 8% on the day. The move came on solid volume too with " \
                          "far more shares changing hands than in a normal session. This stock, which remained " \
                          "volatile and traded within the range of $21.74 –$33.20 in the past one-month time frame, " \
                          "witnessed a sharp increase yesterday. The company's Zacks Consensus Estimate for the " \
                          "current quarter has moved higher over the past few weeks, suggesting that more solid " \
                          "trading could be ahead for Tailored Brands. So make sure to keep an eye on this stock " \
                          "going forward to see if this recent jump can turn into more strength down the road. "
    sample_neutral_article = "After more than a year-and-a half of construction, Sacred Heart Community School is set " \
                             "to open on Monday featuring new gender-neutral washrooms. The washroom stalls will " \
                             "have floor-to-ceiling doors that lock and communal sinks for hand washing. A security " \
                             "camera will also overlook the common sink area, plus the washroom will not have a " \
                             "door covering the entry as it will lead straight into the hallways. Catholic Schools " \
                             "Division communications Twylla West said it’s simply the way washrooms in schools are " \
                             "being built now. “It’s 2017, and things are very different from the last time we were " \
                             "building schools… and this is how they look now,” she said. “You can call it " \
                             "gender neutral, you can give it whatever label you want. We’re just calling it " \
                             "“the washroom.”"
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    for sentence in [sample_bad_article, sample_good_article, sample_neutral_article]:
        vs = analyzer.polarity_scores(sentence)
        print("{:-<65} {}".format(sentence[:10], str(vs)))



if __name__=='__main__':
    x = "run"