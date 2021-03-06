#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', 'six', 'setuptools_scm']

test_requirements = ['pytest', ]

setup(
    author="Matthieu Berthomé",
    author_email='rienafairefr@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="LDraw mklist in Python",
    entry_points={
        'console_scripts': [
            'mklist=mklist.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pymklist',
    name='pymklist',
    packages=find_packages(include=['mklist']),
    setup_requires=setup_requirements,
    use_scm_version=True,
    test_suite='tests',
    tests_require=test_requirements,
    version="1.0.0",
    url='https://github.com/rienafairefr/pymklist',
    zip_safe=False,
)
