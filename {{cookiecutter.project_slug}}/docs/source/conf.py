# -*- coding: utf-8 -*-
#
# {{ cookiecutter.project_slug }} documentation build configuration file, created by
# sphinx-quickstart on {% now 'local', '%a %b %d %H:%M:%S %Y' %}.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import {{ cookiecutter.project_slug.lower().replace(' ', '_').replace('-', '_')}}

here = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(here, '..')))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'{{ cookiecutter.project_name }}'
copyright = u'{% now 'local', '%Y' %}, {{ cookiecutter.copyright_holder }}'
author = u"{{ cookiecutter.full_name.replace('\"', '\\\"') }}"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = {{ cookiecutter.project_slug.lower().replace(' ', '_').replace('-', '_')}}.__version__
# The full version, including alpha/beta/rc tags.
release = {{ cookiecutter.project_slug.lower().replace(' ', '_').replace('-', '_')}}.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'any'  # makes single backticks autofind targets

{% if cookiecutter.apidoc == 'yes' %}
# -- Run apidoc plug-in manually, as readthedocs doesn't support it -------
# See https://github.com/rtfd/readthedocs.org/issues/1139
def run_apidoc(_):
    here = os.path.dirname(__file__)
    out = os.path.abspath(os.path.join(here, 'apidocs'))
    src = os.path.abspath(os.path.join(here, '..', '{{ cookiecutter.project_slug }}'))

    ignore_paths = []

    argv = [
        "-f",
        "-T",
        "-e",
        "-M",
        "-o", out,
        src
    ] + ignore_paths

    try:
        # Sphinx 1.7+
        from sphinx.ext import apidoc
        apidoc.main(argv)
    except ImportError:
        # Sphinx 1.6 (and earlier)
        from sphinx import apidoc
        argv.insert(0, apidoc.__file__)
        apidoc.main(argv)


def setup(app):
    app.connect('builder-inited', run_apidoc)
{% endif %}



# -- Options for extensions -------------------------------------------------

# Only the __init__ method’s docstring is inserted.
autoclass_content = 'init'
# order members by source code order
autodoc_member_order = 'bysource'
# Disable docstring inheritance
autodoc_inherit_docstrings = False
# mock the packges that is not avaiable on your machine
# autodoc_mock_imports = ['cython', 'sqlalchemy', 'matplotlib',
#                         'numpy', 'schema', 'tqdm', 'pandas']

# napoleon
napoleon_numpy_docstring = False
napoleon_use_rtype = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None)
}

# autosummary
# Make _autosummary files and include them
autosummary_generate = True
# autosummary_imported_members = True

# ipython
ipython_warning_is_error = False
ipython_execlines = [
    "import numpy as np",
]
ipython_savefig_dir = '../_build/ipython_savefig'


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = 'nature'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': ['globaltoc.html', 'relations.html', 'searchbox.html'] ,
    'index': ['globaltoc.html', 'searchbox.html']
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = '{{ cookiecutter.project_slug}}_doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, '{{ cookiecutter.project_slug }}.tex', u'{{ cookiecutter.project_name }} Documentation',
     u"{{ cookiecutter.full_name.replace('\"', '\\\"') }}", 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, '{{ cookiecutter.project_slug }}', u'{{ cookiecutter.project_name }} Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, '{{ cookiecutter.project_slug }}', u'{{ cookiecutter.project_name }} Documentation',
     author, '{{ cookiecutter.project_slug }}', "{{ cookiecutter.project_short_description.replace('\"', '\\\"') }}",
     'Miscellaneous'),
]
