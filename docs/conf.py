import os
import sys
sys.path.append(os.path.abspath('..'))

from datetime import datetime
from stringutils import __version__

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
source_suffix = ['.rst']
exclude_patterns = ['_build']

master_doc = 'index'
project = 'stringutils'
copyright = '{} Alex Hunt'.format(datetime.now().year)
author = 'Alex Hunt'
version = __version__
release = version
language = 'en'

html_theme = 'alabaster'
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html'
    ]
}
html_theme_options = {
    'description': 'A functional string utility library for Python',
    'github_user': 'huntie',
    'github_repo': 'stringutils',
    'github_type': 'star',
    'fixed_sidebar': True,
    'sidebar_collapse': False
}
