#!/usr/bin/env python

from setuptools import setup

def readme():
    return open("README.rst").read()

setup(name='libcipher',
      version='0.1.0',
      description=("Python package containing cipher functions"
                   "from the book 'Hacking Secret Ciphers with Python'."),
      long_description=readme(),
      author='Vijay Kumar B.',
      author_email='vijaykumar@bravegnu.org',
      url='http://github.com/chennaipy/libcipher',
      license="BSD 2-Clause",
      packages=['libcipher'],
      test_suite="tests",
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Games/Entertainment :: Puzzle Games',
      ])
