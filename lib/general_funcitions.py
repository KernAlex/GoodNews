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


def fix_url(domain, url):
    """
    :param string: must be a url, no spaces, and no added '?'s
    :return: a clensed url
    >>> domain = 'https://www.gayhar.com'
    >>> url = 'https://www.gayhar.com/totaly/not/porn/?psource=gayporn.com'
    >>> fix_url(domain, url)
    https://www.gayhar.com/totaly/not/porn
    >>> url = 'https://gayhar.com/totaly/not/porn/?psource=gayporn.com'
    >>> fix_url(domain, url)
    Traceback (most recent call last):
    AssertionError: domain https://www.gayhar.com is not in url
    >>> url = '/some/other/part/of/the/page'
    >>> fix_url(domain, url)
    'https://www.gayhar.com/some/other/part/of/the/page'
    >>> url = '/some/other/part/of/the/page'
    """
    if url[0] != '/':
        domain_len = len(domain)
        assert domain in url[:domain_len], 'domain {} is not in url'.format(domain)
    pass



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