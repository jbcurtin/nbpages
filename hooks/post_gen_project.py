#!/usr/bin/env python

import os
import shutil


if '{{ cookiecutter.copy_nbpages }}'.lower() == 'y':
    import nbpages

    nbpages_sourcedir = os.path.realpath(nbpages.__path__[0])
    nbpages_targetdir = os.path.join(os.path.realpath(os.path.curdir), 'nbpages')

    shutil.copytree(nbpages_sourcedir, nbpages_targetdir,
                    ignore=shutil.ignore_patterns('*.pyc', '.*', '__pycache__'))

if '{{ cookiecutter.skip_examples }}'.lower() == 'y':
    for nbdir in ('{{ cookiecutter.example_notebook }}', '{{ cookiecutter.example_subtopic }}'):
        to_remove = os.path.join(os.path.realpath(os.path.curdir), nbdir)
        shutil.rmtree(to_remove)
