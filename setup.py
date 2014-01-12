from distutils.core import setup

setup(
    name='paAPI',
    version='0.0.1',
    author='oznu',
    author_email='dev@oz.nu',
    packages=['paAPI'],
    url='https://github.com/oznu/paAPI',
    license='Apache License',
    description='A python client for the Parallels Operations (POA) and Business Automation (PBA-E) APIs.',
    long_description=open('README.rst').read(),
)
