#!/usr/bin/env python

from setuptools import setup

setup(
    name='repo_maker',
    version='1.0',
    author='William Dean',
    author_email='wdean@homepartners.com',
    description='Quickly create data science repo.',
    packages=['repo_maker'],
    scripts=['scripts/make_repo']
)
