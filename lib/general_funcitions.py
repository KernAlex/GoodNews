import doctest
from bs4 import BeautifulSoup
debug = False


def extract_sentences(string):
    """
    :param string:
    :return: A single string containing sentences it thinks are relevant
    >>> f = open("test_file.txt", "r")
    >>> raw = f.read()
    >>> f.close()
    >>> extract_sentences(raw)[:100]
    ' Published: June 7, 2019 8:17 a.m. ET DocuSign Inc. exceeded expectations with its headline results '
    """
    string = str(string)
    result = ''
    soup = BeautifulSoup(string, 'html.parser')
    paragraphs = soup.find_all('p')
    new_set = []
    for i in paragraphs:
        temp_string = ''
        text = i.get_text()
        for i in text:
            if i == '\n':
                temp_string += ' '
                continue
            elif i == '\r':
                continue
            elif i == '\t':
                temp_string += ' '
                continue
            temp_string += i
        new_set.append(temp_string.replace('  ', ''))
    for string in new_set:
        if sentence_or_add(string):
            if string[len(string) - 1] != ' ':
                result += ' '
            result += string
    return result


def sentence_or_add(string):
    """
    :param string:
    :return: returns True if string is a sentence, otherwise false
    >>> sentence_or_add('Copyright © 2019 MarketWatch, Inc.All rights reserved.')
    False
    >>> sentence_or_add('By using this site you agree to the Terms of Service, Privacy Policy, and Cookie Policy.')
    True
    >>> sentence_or_add('Join the conversation')
    False
    >>> sentence_or_add('Hello.')
    False
    >>> sentence_or_add('Hello World')
    False
    >>> sentence_or_add('Hello World. ')
    True
    >>> sentence_or_add(' Read: Beyond Meat stock soars after first earnings report ')
    False
    """
    if len(string) < 10:
        return False
    punctuation_set = {'!', '.', '?', ']'}
    if '©' in string:
        return False
    for i in range(len(string) - 10, len(string)):
        if string[i] in punctuation_set:
            return True
    return False

clean = []

def fix_url(url):
    """
    :param string: a url of various forms. The purpose of this function
    is to take in a url with potential noise, andd return the specific domain name
    :return: a clensed url
    >>> url = 'https://www.gayhar.com/totaly/not/porn/?psource=gayporn.com'
    >>> fix_url(url)
    ('https://www.gayhar.com', 'https://www.gayhar.com/totaly/not/porn')
    >>> url = 'https://gayhar.com/totaly/not/porn/?psource=gayporn.com'
    >>> fix_url(url)
    ('https://gayhar.com', 'https://gayhar.com/totaly/not/porn')
    >>> url = 'http://www.gayhar.com/totaly/not/porn/?psource=gayporn.com'
    """
    domain = get_domain(u)
    cleaned = ""
    cleaned += clean[0] + clean[1]

    return domain, cleaned





def get_domain(url):
    """
    :param url: a string. could be something ugly like
                'https://github.com/KernAlex/GoodNews/blob/master/lib/article.py', only
                returns the url
    :return:    https://github.com
    >>> url = 'http://www.gayhar.com/totaly/not/porn/?psource=gayporn.com'
    >>> get_domain(url)
    'http://www.gayhar.com'
    >>> get_domain("gayhar.com/ahdfkg")
    'https://gayhar.com'
    >>> url = 'https://www.gayhar.com/totaly/not/porn/?psource=gayporn.com'
    >>> get_domain(url)
    'https://www.gayhar.com'
    """
    from urllib.parse import urlparse
    parse = urlparse(url)
    n = "https://" + parse.netloc

    p = parse.path

    list = []
    if n == "https://":
        clean.append("https://")
        clean.append(p)
        for i in p:
            list.append(i)
            for i in reversed(list):
                if i != "/":
                    del i
                else:
                    del list[-1]
                    q = ""
                    for i in list:
                        q += i
                    q = "https://" + q

                    return q
    else:
        clean.append(n)
        clean.append(p)
        return n

if debug:
    doctest.testmod()

if __name__=="__main__":
    import requests
    my_site = requests.get(
        "https://www.pbs.org/newshour/science/how-bad-is-the-measles-comeback-heres-70-years-of-data")
    text = str(my_site.text)
    print(extract_sentences(text))
    # Gruhar, how to debug one thing at a time: https://stackoverflow.com/questions/10080157/is-it-possible-to-only-test-specific-functions-with-doctest-in-a-module
    doctest.testmod()
