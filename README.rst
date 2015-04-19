libcipher
=========

.. image:: https://travis-ci.org/Chennaipy/libcipher.svg?branch=master
   :target: https://travis-ci.org/Chennaipy/libcipher

.. image:: http://img.shields.io/codecov/c/github/Chennaipy/libcipher.svg?style=flat
   :target: https://codecov.io/github/Chennaipy/libcipher?branch=master

.. image:: https://readthedocs.org/projects/libcipher/badge/?version=latest
   :target: https://readthedocs.org/projects/libcipher/?badge=latest
   :alt: Documentation Status


The goal of this project is to learn and implement the best practices,
in writing and maintaining a Python package. For this purpose, we
implement a Python package containing cipher functions from the book
`"Hacking Secret Ciphers with Python"
<https://inventwithpython.com/hacking/chapters/>`_.

Usage
-----

The package can be installed using the following command ::

  $ pip install git+git://github.com/chennaipy/libcipher.git

Development
-----------

After cloning the repository, create a new virtual environment

$ virtualenv env

Next, activate this environment

$ source env/bin/activate

You can now install the package in development mode using the following command

$ python3 setup.py develop

You can execute the unit tests, using the following command

$ python3 setup.py test

You can build the documentation, using the following commands

$ pip install -r doc-requirements.txt
$ cd doc
$ make html

Contributing Guidelines
-----------------------

Before sending a pull request, please ensure the following:

* The code has been checked for `PEP8
  <https://www.python.org/dev/peps/pep-0008/>`_ compliance using the
  ``pep8`` tool.

* Unit test cases have been added for the new functionality, and the
  line coverage is 100%.

* Docstrings have been added to public functions, that they adhere to
  `Google Docstring Convention
  <https://google-styleguide.googlecode.com/svn/trunk/pyguide.html>`_.

* The API manual has been updated, to display the documentation for
  any new modules added.

* The changelog has been updated, to indicate the change made along
  with the issue no. on GitHub. The changelog is to be in `releases
  format <http://releases.readthedocs.org/en/latest/index.html>`_.
