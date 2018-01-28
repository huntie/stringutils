from codecs import open
from setuptools import setup
from stringutils import __version__

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='stringutils',
    description='A functional string utility library for Python',
    long_description=long_description,
    version=__version__,
    url='https://github.com/huntie/stringutils',
    author='Alex Hunt',
    author_email='hello@alexhunt.io',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],

    keywords='string helpers transform',
    packages=['stringutils']
)
