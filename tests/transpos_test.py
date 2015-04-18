"""Unit tests for reverse cipher module."""

import unittest
from libcipher.transpos import encrypt

class TransposEncryptTestCase(unittest.TestCase):
    def test_keysizeLessthanHalfMessageSize(self):
        encrypted = encrypt(3,'Hello World')
        self.assertEqual(encrypted, "HlWleoodl r|")
    
    def test_keysizeGreaterThanHalfMessageSize(Self):
        encrypted = encrypt(6,'Hello World')
        #Exception Has to be thrown indicating Key Size Criteria