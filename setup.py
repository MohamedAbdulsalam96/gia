# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in gia/__init__.py
from gia import __version__ as version

setup(
	name='gia',
	version=version,
	description='General Investment Authority',
	author='Ahmed Mohammed Alkuhlani',
	author_email='aalkuhlani95@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
