import os

from setuptools import setup

PACKAGE_VERSION = '0.3'


def version():
    if os.getenv('TRAVIS'):
        return os.getenv('TRAVIS_BUILD_NUMBER')
    else:
        import odintools

        return odintools.version(PACKAGE_VERSION, os.environ.get('BUILD_NUMBER'))


setup(
    name='osaapi',
    version_getter=version,
    author='apsliteteam, oznu',
    author_email='aps@odin.com',
    packages=['osaapi'],
    url='https://aps.odin.com',
    license='Apache License',
    description='A python client for the Odin Service Automation (OSA) and billing APIs.',
    long_description=open('README.md').read(),
    setup_requires=['odintools'],
    odintools=True,
)
