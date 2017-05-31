#!/usr/bin/env python

from setuptools import setup


setup(
    name='osaapi',
    version='0.4.0',
    author='apsconnect team, original by oznu',
    author_email='aps@odin.com',
    packages=['osaapi'],
    url='https://aps.odin.com',
    license='Apache License',
    description='A python binding for the Odin Service Automation (OSA) and billing APIs.',
    long_description=open('README.md').read(),
)
