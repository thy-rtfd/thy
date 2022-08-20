# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

from pathlib import Path

cur_path = Path(__file__).resolve().parent
sys.path.insert(0, os.path.abspath('.'))

project = "Thy's Notes"
project_copyright = '2021, Thierry Humphrey'
author = 'Thierry Humphrey'

manpages_url = 'https://linux.die.net/man/{section}/{page}'
numfig = True

rst_prolog = """
.. role:: python(code)
    :language: python

"""

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    # 'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'sphinx.ext.githubpages',

    'myst_parser',
]

templates_path = ['_templates']

exclude_patterns = []

html_show_sphinx = False
html_show_copyright = False

# https://sphinx-themes.org/sample-sites/furo/
# https://pradyunsg.me/furo/
html_theme = 'furo'
html_title = "Thy's Notes"

html_theme_options = {
    'navigation_with_keys': True,
    # 'sidebar_hide_name'   : True,
}

html_js_files = [
    'js/custom.js'
]
html_show_sourcelink = False
html_static_path = ['_static']
# html_extra_path = [
#     # Docutils
#     # 'public_docs/docutils/user/rst/quickref.html',
# ]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md' : 'markdown',
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

intersphinx_mapping = {
    'py3'       : ('https://docs.python.org/3', None),
    'sphinx'    : ('https://www.sphinx-doc.org/en/master/', None),
    'numpy'     : ('https://numpy.org/doc/stable', None),
    'pandas'    : ('https://pandas.pydata.org/pandas-docs/stable', None),
    'pydevguide': ('https://devguide.python.org', None),
}
