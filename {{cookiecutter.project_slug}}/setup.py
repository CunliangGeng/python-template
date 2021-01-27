#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit CITATION.cff
with open('CITATION.cff', 'r') as cff:
    for line in cff:
        if 'version:' in line:
            version = line.replace('version:', '').strip().strip('"')

with open('README.md') as readme_file:
    readme = readme_file.read()

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3 or later': 'License :: OSI Approved :: GNU General Public License'
} %}

setup(
    name='{{ cookiecutter.project_slug.lower().replace(' ', '_').replace('-', '_')}}',
    version=version,
    description="{{ cookiecutter.project_short_description.replace('\"', '\\\"') }}",
    long_description=readme + '\n\n',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(),
    include_package_data=True,  # check MANIFEST.in
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[ #check details https://pypi.org/classifiers/
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    install_requires=[],  # FIXME: add your package's dependencies to this list
    extras_require={
        'dev': ['prospector[with_pyroma]', 'autopep8', 'isort', 'twine'],
        'doc': ['sphinx', 'ipython'],
        'test': ['pytest', 'pytest-cov', 'pytest-runner', 'pycodestyle',
                'coverage', 'codacy-coverage', 'coveralls'],
    }
)
