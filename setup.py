import os

from setuptools import setup

PACKAGE_VERSION = '0.3'


def version():
    def version_file(mode='r'):
        return open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'version.txt'), mode)

    if os.getenv('TRAVIS'):
        with version_file('w') as verfile:
            verfile.write('{0}.{1}'.format(PACKAGE_VERSION, os.getenv('TRAVIS_BUILD_NUMBER')))
    with version_file() as verfile:
        data = verfile.readlines()
        return data[0].strip()


setup(
    name='osaapi',
    version=version(),
    author='apsliteteam, oznu',
    author_email='aps@odin.com',
    packages=['osaapi'],
    url='https://aps.odin.com',
    license='Apache License',
    description='A python client for the Odin Service Automation (OSA) and billing APIs.',
    long_description=open('README.md').read(),
)
