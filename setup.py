#!/usr/bin/env python

from setuptools import setup


setup(
    name='osaapi',
    version='1.0.0',
    author='apsconnect team, original by oznu',
    author_email='aps@odin.com',
    packages=['osaapi'],
    url='https://aps.odin.com',
    license='Apache License',
    description='A python binding for the Odin Service Automation (OSA) and billing APIs.',
    long_description=open('README.md').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
    ],
)
