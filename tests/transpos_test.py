# -*- coding: utf-8 -*-
"""Unit tests for tranpos cipher module-encrypt function."""

import unittest
from libcipher.transpos import encrypt


class TransposEncryptTestCase(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
