'''
setup.py   file is an essential part of packaging and
 distributing Python projects. It contains metadata about the project, such as its name, version, author, and dependencies. The setup.py file is used by tools like setuptools to build and install the package.
Here's a basic example of what a setup.py file might look like:
```python'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from a file and return them as a list."""
    requirement_lst = []
    try:
        with open('requirements.txt','r') as file:
            # Read the lines from the file and return them as a list
            lines = file.readlines()
            #process each line
            for line in lines:
                #strip whitespace and newline characters
                requirement = line.strip()
                #ignore empty lines and comments and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst
print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Tharun',
    author_email='tharun@example.com',
    packages=find_packages(),
    install_requires=get_requirements(),)