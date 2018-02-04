stringutils
===========

A functional string utility library for Python 2 and 3. Closely inspired by implementations in Haskell and PHP.

For more documentation, please see `http://stringutils.readthedocs.io <http://stringutils.readthedocs.io/en/develop/>`_.

.. note::
    This package is still in an early development stage, and it is possible that the naming and API of some functions will change.

Features
--------

The main design goal of this library is to provide helpful string functions which complement what can already be done with *str*, *str.format* and *textwrap*. As such, it includes:

- A selective set of additional string helper functions.
- Extended versions of existing *str* methods as functions where useful.

Installation
------------

Install the latest release from `PyPI <https://pypi.org/project/stringutils/>`_:

.. code-block:: sh

    pip install stringutils

Usage
-----

All functions are available directly off the :code:`stringutils` package. You may choose to import individual functions by name, or import all.

.. code-block:: python

    from stringutils import reverse, unwords, words

    def reverse_words(string):
        return unwords(map(reverse, words(string)))

Contribute
----------

- Source code: https://github.com/huntie/stringutils
- Issue tracker: https://github.com/huntie/stringutils/issues

License
-------

The project is licensed under the MIT license.
