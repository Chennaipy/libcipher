"""Unit tests for reverse cipher module."""

import unittest
from libcipher.transpos import encrypt
from libcipher.transpos import InvalidKeySizeException


class TransposEncryptTestCase(unittest.TestCase):
    def test_keysizeLessthanHalfMessageSize(self):
        encrypted = encrypt(3, 'Hello World')
        self.assertEqual(encrypted, "HlWleoodl r|")

    def test_empty(self):
        encrypted = encrypt(3, '')
        self.assertEqual(encrypted, "|")

    def test_keysizeGreaterThanHalfMessageSize(self):
        with self.assertRaises(InvalidKeySizeException):
            encrypt(7, 'Hello')
if __name__ == '__main__':
    unittest.main()
