"""
    stringutils
    ~~~~~~~~~~~

    A functional string utility library for Python.

    :copyright: (c) 2018 Alex Hunt.
    :license: MIT, see LICENSE.txt for more details.
"""

import re

def join(strings, sep=', ', insertend=False):
    """
    Concatenate a list of strings into a single string by a separating
    delimiter. If *insertend* is given and true, the delimiter is also included
    at the end of the string.
    """
    return sep.join(strings) + (sep if insertend else '')

def lines(string, keepends=False):
    """
    Split a string into a list of strings at newline characters. Unless
    *keepends* is given and true, the resulting strings do not have newlines
    included.
    """
    return string.splitlines(keepends)

def reverse(string):
    """
    Reverse the order of the characters in a string.
    """
    return string[::-1]

def words(string):
    """
    Split a string into a list of words, which were delimited by one or more
    whitespace characters.
    """
    return re.split('\s+', string)

def unlines(lines):
    """
    Join a list of lines into a single string after appending a terminating
    newline character to each.
    """
    return join(lines, '\n', True)

def unlines_universal(lines):
    """
    Join a list of lines into a single string after appending a terminating
    CRLF newline sequence to each.
    """
    return join(lines, '\r\n', True)

def unwords(words):
    """
    Join a list of words into a single string with separating spaces.
    """
    return join(words, ' ')
