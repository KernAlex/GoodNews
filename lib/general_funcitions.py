import doctest
from bs4 import BeautifulSoup
debug = False

def remove_brackets(string):
    """
    :param string: input of a string usually containg css code with brackets.
    :return:
    >>> s = '<a href="https://www.somecreap.com"> {function : do some stuff} <p> some text </p>'
    >>> remove_brackets(s)
    '<a href="https://www.somecreap.com">  <p> some text </p>'
    >>> s = 'this { is { some {} {nested} bracket} stuff} test'
    >>> remove_brackets(s)
    'this  test'
    >>> s = 'The file { didnt end with this bracket, { but it should still work'
    >>> remove_brackets(s)
    'The file '
    """
    brackets_seen = 0
    result = ''
    for i in string:
        if i == '{':
            brackets_seen += 1
        elif i == '}':
            brackets_seen -= 1
            continue
        if brackets_seen <= 0:
            result += i
    return result


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

if debug:
    doctest.testmod()

if __name__=="__main__":
    import requests
    my_site = requests.get(
        "https://www.pbs.org/newshour/science/how-bad-is-the-measles-comeback-heres-70-years-of-data")
    text = str(my_site.text)
    print(extract_sentences(text))
    doctest.testmod()