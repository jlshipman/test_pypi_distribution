# First Package Attempt

## Pre-Requististes

- program
  - twine
  - tree

- apple
  - get from homebrew 
  
## Instructions

Directory setup

- __hello_word__
  - Pipfile
  - command_line.py
  - __hello_word__
    - README.md
    - __init__.py
    - setup.py


## setup.py

```
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

```

- Notice:  
  - read in README.md file for long description
  - exclude all tests* and testing* from package

# Create Distribution

python3 setup.py bdist_wheel

# Using twine

- python3 -m pip install --upgrade twine
- python3 -m twine upload --repository testpypi dist/*
  - You will be prompted for a username and password. For the username, use __token__. For the password, use the token value, including the pypi- prefix.

twine upload -r testpypi dist/*