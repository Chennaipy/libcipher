# -*- coding: utf-8 -*-
"""Unit tests for tranpos cipher module-encrypt function"""

import unittest
from libcipher.transpos import encrypt
from libcipher.transpos import InvalidKeySizeException


class TransposEncryptTestCase(unittest.TestCase):
    """TransposEncryptTestCase contains test cases for transpose encryption
    """
    def test_keysizeLessthanHalfMessageSize(self):
        """ To test encryption when keysize is lesser than half of message size
        """
        encrypted = encrypt(3, 'Hello World')
        self.assertEqual(encrypted, "HlWleoodl r|")

    def test_empty(self):
        """To test encryption when an empty message('') is given as input
        """
        encrypted = encrypt(3, '')
        self.assertEqual(encrypted, "|")

    def test_keysizeGreaterThanHalfMessageSize(self):
        """To test raise of an exception when keysze is invalid
        """
        self.assertRaises(InvalidKeySizeException, encrypt, 7, 'Hello World')

if __name__ == '__main__':
    unittest.main()
