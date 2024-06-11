from setuptools import setup, find_packages

VERSION = '1.0.1'
DESCRIPTION = 'Encrypt and Decrypt text'

with open("README.md", "r") as f:
    long_description = f.read()

# Setting up
setup(
    name="ciphers-module",
    version=VERSION,
    author="Avyukt27",
    author_email="<avyukt.aggarwal007@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'cipher', 'encode', 'encrypt', 'decrypt', 'decode'],
)