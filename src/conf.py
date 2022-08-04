# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from conf_global import *

html_title = "Thy"
project = "Thy's Notes"
project_copyright = '2022, Thierry Humphrey'
author = 'Thierry Humphrey'

intersphinx_mapping_enabled = (
    # 'thy_main',
    # 'thy_python',
    # 'thy_azure',
    # 'thy_devops',
    # 'thy_qknotes',
    # 'thy_systems',
    # 'thy_misc',

    'py3',
    'pydevguide',
    'rtfd',
    'sphinx',
    'furo',
)
intersphinx_mapping = {k: v for k, v in intersphinx_mapping.items() if k in intersphinx_mapping_enabled}
