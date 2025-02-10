# This file is connected to the requirement.txt because it install the project as an editable package
from setuptools import setup,find_packages

setup(
    name = "us_visa",       # Name of the package (your project name)
    version = "0.0.0",      # Initial version of the package
    author = 'Ayaz',        # Your name as the package author
    author_email="ayazr425@gmail.com",  # Your email address
    packages=find_packages()  # Automatically finds all Python packages inside the project
)

# Note---------------

# setup.py ------is used to make your project a Python package.
# find_packages() -------automatically finds all sub-packages.
# Used after requirements.txt------- because it packages the project after dependencies are installed.
# Allows you to install your project locally using pip install ..

