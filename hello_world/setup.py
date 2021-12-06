from setuptools import setup
from setuptools import find_packages

with open('README.md') as _file:
    long_description = _file.read()

setup(
    name='hello_world',
    version='1.0.0',
    long_description=long_description,
    license='Absolutely no warranty',
    description='this package contains some sample hello world',
    author='Jeffery Shipman',
    author_email='jeffery.shipman@gmail.com',
    url='https://github.com/jlshipman/hello_world',
    packages=find_packages(exclude=('tests*', 'testing*')),
    entry_points={
        'console_script': ['hello_world_cli = hello_world.command_line:main']
    }
)
