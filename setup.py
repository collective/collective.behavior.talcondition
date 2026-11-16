# -*- coding: utf-8 -*-
"""Installer for the collective.behavior.talcondition package."""

from setuptools import find_namespace_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n\n' +
    open('CHANGES.rst').read()
    + '\n\n')


setup(
    name='collective.behavior.talcondition',
    version='1.1.4.dev0',
    description="This package contains a Dexterity behavior and AT schemaextender to add a TAL condition on a content type.",
    long_description=long_description,
    # Get more from https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Zope Plone',
    author='IMIO',
    author_email='dev@imio.be',
    url='http://pypi.python.org/pypi/collective.behavior.talcondition',
    license='GPL V2',
    packages=find_namespace_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.10',
    install_requires=[
        'plone.api',
        'setuptools',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.robotframework',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
