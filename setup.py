from distutils.core import setup
import os

PACKAGE_VERSION = '0.1'


def version():
    import odintools

    return odintools.version(PACKAGE_VERSION, os.environ.get('BUILD_NUMBER'))

setup(
    name='paAPI',
    author='oznu',
    author_email='dev@oz.nu',
    packages=['paAPI'],
    url='https://github.com/oznu/paAPI',
    license='Apache License',
    description='A python client for the Parallels Operations (POA) and Business Automation (PBA-E) APIs.',
    long_description=open('README.rst').read(),
    setup_requires=['odintools'],
    odintools=True,
)
