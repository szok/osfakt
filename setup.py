# -*- coding: utf-8 -*-
import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='osfakt',
    version='0.1',
    packages=['src.osfakt'],
    include_package_data=True,
    license='BSD License',
    description='Django apps to invoice',
    long_description=README,
    url='http://www.webcoding.pl',
    author='Piotr Jarolewski',
    author_email='jarolewski.piotr@gmail.com',
    classifiers=[
        'Framework :: Django',
        ],
    install_requires=[
        'django>=1.8',
    ]
)
