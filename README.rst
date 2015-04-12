libcipher
=========

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

After cloning the repository, install the package in development mode
using the following command ::

  $ python3 setup.py develop

You can execute the unit tests, using the following command ::

  $ python3 setup.py test

You can build the documentation, using the following commands ::

  $ pip install -r doc-requirements.txt
  $ cd doc
  $ make html
