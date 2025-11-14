# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
nbsphinx_kernel_name = 'python3'


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pygbm'
copyright = '2025, Randa He'
author = 'Randa He'
release = 'beta'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc', #automatically generats documentation from Python docstrings
#   	'nbsphinx', #useful if i am documenting Jupyter notebooks
#	'sphinx.ext.mathjax', #renders LaTex math formulas in docs using MathJax
	'sphinx_rtd_theme', #give the documentation 'read the docs' theme
#    'sphinx_gallery.load_style',  # load CSS for gallery (needs SG >= 0.6)
 #   'sphinx.ext.githubpages', #adds a file to ensure docs build properly on github pages
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Add GitHub repository settings
html_theme_options = {
    'repository_url': 'https://github.com/randa1029/pygbm',
    'use_repository_button': True,
}