#!/usr/bin/env python
# coding: utf8

from setuptools import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='pef',
    version='0.1.0',
    keywords=['pip', 'dependency'],
    description='Yet another .gitignore magician in your command line.',
    long_description=readme,
    author='cls1991',
    author_email='tzk19910406@hotmail.com',
    url='https://github.com/cls1991/pef',
    py_modules=['pef'],
    install_requires=[
        'click>=6.7',
        'colorama>=0.3.9'
    ],
    license='Apache License 2.0',
    zip_safe=False,
    entry_points={
        'console_scripts': ['pef = pef:cli']
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent'
    ]
)
