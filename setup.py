from setuptools import setup

# In the olden days all package set up in the setup.py file.
# This is a security risk as arbitrary code can be run in the setup file
# Now it basically just contains this small bit of code, the rest goes in the setup.cfg file

if __name__ == "__main__":
    setup()