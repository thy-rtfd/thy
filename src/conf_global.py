html_title = "<a href='https://thy.readthedocs.io'>home</a>"

# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
# https://www.sphinx-doc.org/en/master/examples.html
intersphinx_mapping = {
    # 'thy_main'         : ('https://thy.readthedocs.io/', None),
    # 'thy_python'       : ('https://thy-python.readthedocs.io/', None),
    # 'thy_azure'        : ('https://thy-azure.readthedocs.io/', None),
    # 'thy_devops'       : ('https://thy-devops.readthedocs.io/', None),
    # 'thy_qknotes'      : ('https://thy-qknotes.readthedocs.io/', None),
    # 'thy_systems'      : ('https://thy-systems.readthedocs.io/', None),
    # 'thy_misc'         : ('https://thy-misc.readthedocs.io/', None),

    'sphinx'           : ('https://www.sphinx-doc.org/en/master/', None),
    'jupyterbook'      : ('https://jupyterbook.org/en/stable/', None),
    'myst_parser'      : ('https://myst-parser.readthedocs.io/en/latest/', None),
    'myst_nb'          : ('https://myst-nb.readthedocs.io/en/latest/', None),
    'sphinx_book_theme': ('https://sphinx-book-theme.readthedocs.io/en/stable/', None),
    'furo'             : ('https://pradyunsg.me/furo/', None),

    'py3'              : ('https://docs.python.org/3/', None),
    'numpy'            : ('https://numpy.org/doc/stable/', None),
    'pandas'           : ('https://pandas.pydata.org/pandas-docs/stable', None),
    'pydevguide'       : ('https://devguide.python.org/', None),
    'python_guide_org' : ('https://docs.python-guide.org/', None),
    'django'           : ('https://docs.djangoproject.com/en/3.2/', 'https://docs.djangoproject.com/en/3.2/_objects/'),
    'jinja'            : ('https://jinja.palletsprojects.com/en/3.1.x/', None),
    'requests'         : ('https://requests.readthedocs.io/en/latest/', None),
    'podman'           : ('https://docs.podman.io/en/stable/', None),
    'molecule'         : ('https://molecule.readthedocs.io/en/stable/', None),
    'bs4'              : ('https://www.crummy.com/software/BeautifulSoup/bs4/doc/', None),
    'buildbot'         : ('https://docs.buildbot.net/latest/', None),
    'pypa'             : ('https://www.pypa.io/en/latest/', None),
    'waf'              : ('https://waf.io/apidocs/', None),
    'setuptools'       : ('https://setuptools.pypa.io/en/latest/', None),
    'ansible'          : ('https://docs.ansible.com/ansible/latest/', None),
    'conda'            : ('https://conda.io/en/latest/', None),
    'dnf'              : ('https://dnf.readthedocs.io/en/latest/', None),
    'pip'              : ('https://pip.pypa.io/en/stable/', None),
    'pelican'          : ('https://docs.getpelican.com/en/latest/', None),
    'rtfd'             : ('https://docs.readthedocs.io/en/stable/', None),
    'wagtail'          : ('https://docs.wagtail.org/en/stable/', None),
    'boto3'            : ('https://boto3.amazonaws.com/v1/documentation/api/latest/', None),
    'ceph'             : ('https://docs.ceph.com/en/latest/', None),
    'psycopg'          : ('https://www.psycopg.org/docs/', None),
    'sqlalchemy'       : ('https://docs.sqlalchemy.org/en/14/', None),

    'blender'          : ('https://docs.blender.org/manual/en/latest/', None),
    'blenderapi'       : ('https://docs.blender.org/api/current/', None),

    'circuitpython'    : ('https://docs.circuitpython.org/en/latest/', None),
    'micropython'      : ('https://docs.micropython.org/en/latest/', None),

    # ''     : ('', None),
    # ''     : ('', None),

    # objects.inv is not found
    # 'pygments'   : ('https://pygments.org/docs/', None),
    # 'selenium'   : ('https://www.selenium.dev/documentation/', None),
    # 'opencv'     : ('https://docs.opencv.org/4.x/', None),
}

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
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',

    'myst_parser',

    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",

]

templates_path = [
    '_global/_templates',
    '_templates',
]

exclude_patterns = []

html_show_sphinx = False
html_show_copyright = False

# https://pradyunsg.me/furo/
html_theme = 'furo'

html_theme_options = {
    'navigation_with_keys': True,
    # 'sidebar_hide_name'   : True,
}

html_css_files = [
    '_global/custom.css',
]
html_js_files = [
    '_global/custom.js',
]
html_show_sourcelink = False
html_static_path = ['_static']
html_extra_path = []

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
myst_heading_anchors = 3

autosectionlabel_prefix_document = True
