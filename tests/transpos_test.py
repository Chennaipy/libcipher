# -*- coding: utf-8 -*-
"""Unit tests for tranpos cipher module."""

import unittest
from libcipher.transpos import encrypt
from libcipher.transpos import decrypt


class EncryptTestCase(unittest.TestCase):
    """Test cases for transpose encryption."""
    def test_simple(self):
        """Test positive scenario."""
        encrypted = encrypt(3, 'Hello World')
        self.assertEqual(encrypted, "HlWleoodl r")

    def test_empty(self):
        """Test ValueError is raised for empty message."""
        self.assertRaises(ValueError, encrypt, 1, '')

    def test_invalid_key(self):
        """Test ValueError is raise for key size < half message size."""
        self.assertRaises(ValueError, encrypt, 7, 'Hello World')


class DecryptTestCase(unittest.TestCase):
    """Test cases for transpose decryption."""
    def test_decrypt(self):
        decrypted = decrypt(8, 'Cenoonommstmme oo snnio. s s c')
        self.assertEqual(decrypted, 'Common sense is not so common.')


if __name__ == '__main__':
    unittest.main()
