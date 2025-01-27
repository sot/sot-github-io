# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ska'
copyright = '2025, Smithsonian Astrophysical Observatory'
author = 'Tom Aldcroft'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = []

templates_path = ['_templates']

# Version information from the package.
version = "1.0"
release = version

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ---------------------------------------------------
html_baseurl = "https://sot.github.io"

# The theme to use for HTML and HTML Help pages.
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/sot/sot-github-io",
            "icon": "fab fa-github-square",
        },
    ],
    "navbar_start": ["navbar-project-version"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "secondary_sidebar_items": ["page-toc"],
}

# No left sidebar
html_sidebars = {
  "**": []
}
