from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Encrypt and Decrypt text'
LONG_DESCRIPTION = 'A package that allows encryption and decryption of text using methods.'

# Setting up
setup(
    name="ciphers",
    version=VERSION,
    author="Avyukt27",
    author_email="<avyukt.aggarwal007@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'cipher', 'encode', 'encrypt', 'decrypt', 'decode'],
    classifiers=[
        "Development Status :: 3 - First Release",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)