# -*- coding: utf-8 -*-
"""Installer for the collective.behavior.talcondition package."""

from setuptools import setup


long_description = (
    open('README.md').read()
    + '\n\n' +
    open('CONTRIBUTORS.md').read()
    + '\n\n' +
    open('CHANGES.md').read()
    + '\n\n')


setup(
    name='collective.behavior.talcondition',
    version='1.1.4.dev0',
    description="This package contains a Dexterity behavior and AT schemaextender to add a TAL condition on a content type.",
    long_description=long_description,
    long_description_content_type='text/markdown',
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
        "Programming Language :: Python :: 3.14",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Zope Plone',
    author='IMIO',
    author_email='dev@imio.be',
    url='http://pypi.python.org/pypi/collective.behavior.talcondition',
    license='GPL V2',
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.10',
    install_requires=[
        'plone.api',
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
