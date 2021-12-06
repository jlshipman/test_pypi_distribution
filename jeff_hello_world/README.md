# First Package Attempt

## Pre-Requististes

- program
  - twine
  - tree

- apple
  - get from homebrew 
  
## Instructions

Directory setup

- __jeff_hello_word__
  - Pipfile
  - command_line.py
  - __jeff_hello_word__
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
    name='jeff_hello_world',
    version='1.0.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
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
    - using a markdown file requires
      - long_description_content_type='text/markdown',
  - exclude all tests* and testing* from package

# Create Distribution

python3 setup.py bdist_wheel

# Using twine

- python3 -m pip install --upgrade twine
- python3 -m twine upload --repository testpypi dist/*
  - You will be prompted for a username and password. 
    - For the username, use __token__. 
    - For the password, use the token value, including the pypi- prefix.
  - repository may be set in the .pypirc file 
    - have not got this to work
```
[distutils]
index-servers = testpypi

[testpypi]
username = __token__
password = pypi-AgENdGVzdC5weXBpLm9yZwIkNjA2ZGJiNTMtMDMwMi00
repository = https://test.pypi.org/legacy/
```