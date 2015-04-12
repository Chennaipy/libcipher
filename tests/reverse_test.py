"""Unit tests for reverse cipher module."""

import unittest
from libcipher.reverse import encrypt

class ReverseTestCase(unittest.TestCase):
    def test_simple(self):
        encrypted = encrypt("Hello World")
        self.assertEqual(encrypted, "dlroW olleH")

    def test_empty(self):
        encrypted = encrypt("")
        self.assertEqual(encrypted, "")
        
    
