# -*- coding: utf-8 -*-
"""Installer for the nativeberries.content package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='nativeberries.content',
    version='0.1',
    description="Product that contains all Native Berries content types.",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3.5",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone',
    author='Rafahela',
    author_email='rafahela@gmail.com',
    url='http://pypi.python.org/pypi/nativeberries.content',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['nativeberries'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'z3c.jbot',
        'five.grok',
        'plone.autoform',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
            'plone.app.dexterity [grok, relations]',
            'plone.dexterity',
            'plone.directives.dexterity',
            'plone.directives.form',
            'plone.namedfile',
            'plone.formwidget.namedfile',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
