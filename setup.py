# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 13:10:24 2022

@author: thuds
"""

from setuptools import setup, find_packages

requirements = ["biopython>=1.78", "numpy>=1.21", "regex>=2022.7.9", "pandas>=1.4.4"]


setup(
    name="NNseq",
    version="0.0.1",
    author="Taylor Hudson",
    description="NGS analysis of degenerate off-target sequences",
    long_description='readme',
    long_description_content_type="text/markdown",
    url="https://github.com/ACTG802/NNseq.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)