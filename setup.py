#!/usr/bin/python3

from setuptools import setup, find_packages

requirements = open("requirements.txt").read()

setup(
    name="Utility to pull data from s3 and dump into mongodb",
    version="0.0.1",
    description="It reads current data from s3 and then write it into mongodb.",
    author="Imteyaz Ahmad",
    author_email="ahmad.imt07@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)