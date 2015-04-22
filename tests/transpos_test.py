"""Unit tests for tranpos cipher module-encrypt function"""

import unittest
from libcipher.transpos import encrypt
from libcipher.transpos import InvalidKeySizeException
from libcipher.transpos import NoKeyGivenException
from libcipher.transpos import NoMessageGivenException


class TransposEncryptTestCase(unittest.TestCase):
    def test_keysizeLessthanHalfMessageSize(self):
        encrypted = encrypt(3, 'Hello World')
        self.assertEqual(encrypted, "HlWleoodl r|")

    def test_empty(self):
        encrypted = encrypt(3, '')
        self.assertEqual(encrypted, "|")

    def test_keysizeGreaterThanHalfMessageSize(self):
        self.assertRaises(InvalidKeySizeException, encrypt, 7, 'Hello World')

    def test_NoKeyGiven(self):
        self.assertRaises(NoKeyGivenException, encrypt, None, 'Hello World')

    def test_NoMessageGiven(self):
        self.assertRaises(NoMessageGivenException, encrypt, 3, None)

if __name__ == '__main__':
    unittest.main()
