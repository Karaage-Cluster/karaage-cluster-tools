#!/usr/bin/env python
# Copyright 208-2014 VPAC
#
# This file is part of python-alogger.
#
# python-alogger is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-alogger is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-alogger  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

with open('VERSION.txt', 'r') as f:
    version = f.readline().strip()

setup(
    name="karaage-cluster-tools",
    version=version,
    url='https://github.com/Karaage-Cluster/karaage-cluster-tools',
    author='Brian May',
    author_email='brian@v3.org.au',
    description='Karaage cluster management tools',
    packages=find_packages(),
    license="GPL3+",
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
            "GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="karaage",
    install_requires=['python-alogger', ],
    data_files=[
        ('/etc/karaage3', ['etc/karaage-cluster-tools.cfg', ]),
    ],
    scripts=[
        'sbin/kg-send-usage'
    ],
)
