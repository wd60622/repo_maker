#!/usr/bin/env python

from setuptools import setup

setup(
    name="repo_maker",
    version="0.1.5",
    author="William Dean",
    author_email="wdean@homepartners.com",
    description="Quickly create data science repo.",
    packages=["repo_maker", "repo_maker/files"],
    scripts=["scripts/make_repo"],
    package_data={"": ["*"]},
    include_package_data=True,
    install_requires=["rich"],
)
