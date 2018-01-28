"""
    stringutils
    ~~~~~~~~~~~

    A functional string utility library for Python.

    :copyright: (c) 2018 Alex Hunt.
    :license: MIT, see LICENSE.txt for more details.
"""

__version__ = '0.2.0'

import re

def concat(strings):
    """
    Concatenate a list of strings into a single string.
    """
    return ''.join(strings)

def camel_case(string):
    """
    Convert a string identifier to :code:`camelCase`.
    """
    return lcfirst(pascal_case(string))

def dashed_case(string):
    """
    Convert a string identifier to :code:`dashed-case`. If the string is in
    :code:`snake_case`, capitalization of words will be preserved.
    """
    return join(split_identifier(string), '-')

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

def lcfirst(string):
    """
    Convert the first character of a string to lowercase.
    """
    return string[:1].lower() + string[1:]

def pascal_case(string):
    """
    Convert a string identifier to :code:`PascalCase`.
    """
    return concat(map(ucfirst, split_identifier(string)))

def reverse(string):
    """
    Reverse the order of the characters in a string.
    """
    return string[::-1]

def snake_case(string):
    """
    Convert a string identifier to :code:`snake_case`. If the string is in
    :code:`dashed-case`, capitalization of words will be preserved.
    """
    return join(split_identifier(string), '_')

def split_identifier(string):
    """
    Split a string identifier into a list of its subparts.
    """
    return (
        re.split('[ \-_]', string)
            if re.findall('[ \-_]', string)
            else words(re.sub(r'([a-z])([A-Z0-9])', r'\1 \2', string))
    )

def title_case(string):
    """
    Convert a string identifier to :code:`Title Case`.
    """
    return join(map(ucfirst, split_identifier(string)), ' ')

def words(string):
    """
    Split a string into a list of words, which were delimited by one or more
    whitespace characters.
    """
    return re.split('\s+', string)

def ucfirst(string):
    """
    Convert the first character of a string to uppercase.
    """
    return string[:1].upper() + string[1:]

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
