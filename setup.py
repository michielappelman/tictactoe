from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tictactoe',
    version='0.1',
    description='Tic-tac-toe Game',
    long_description=readme,
    author='Michiel Appelman',
    author_email='michiel@appelman.se',
    url='https://github.com/michielappelman/tictactoe',
    license=license,
    packages=find_packages(exclude=('tests'))
)
