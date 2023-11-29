# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Halcyon'
copyright = '2023, Erich Bremer'
author = 'Erich Bremer'

# The full version, including alpha/beta/rc tags
release = '0.8.0'
version = '0.8.0'

master_doc = 'index'
html_static_path = ['_static']
html_logo = 'docs/images/halcyon.png'
html_favicon = 'docs/images/halcyon.ico'
html_show_sphinx = False
html_show_sourcelink = False

html_theme_options = {
        'style_nav_header_background': 'white',
        'prev_next_buttons_location': 'None',
        'display_version': 'False',
        #'logo': 'halcyon.png',
        #'show_powered_by': 'false',
        #'logo_name': 'false',
        #'github_banner': 'true',
        #'fixed_sidebar': 'true',
        #'github_button': 'true',
        #'github_repo': 'Halcyon',
        #'github_user': 'halcyon-project'
}

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx.ext.autosectionlabel',
#    'sphinx_search.extension'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build','README.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinxawesome_theme'
html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
#html_theme = 'pyramid'

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist"
]
