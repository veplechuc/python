#!/usr/bin/env python3

"""
    shebang is used for linux environment to support executing the file
"""

"""
    Examples modules
"""

from urllib.request import urlopen

import sys


def fetch_words(url):
    """Fetch a list of words from the url

        Args:
            list of iterable items

        Returns:
            list of items
    """
    with urlopen(url) as story:
        story_words =[]
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_as_array(argument):
    """prints the argument passed as it is"""
    print(argument)


def print_using_for(argumen):
    """print the passed argument using for loop"""
    for dat in argumen:
        print(dat)


def main(url):
    data = fetch_words()
    print_as_array(data)

if __name__ == '__main__':
    main(sys.argv[1]) #the 0th argv is the module filename
