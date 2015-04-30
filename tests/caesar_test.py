"""Unit tests for caesar cipher module. """

import unittest
from libcipher.caesar import encrypt, decrypt


class CaesarTestCase(unittest.TestCase):

    def test_encrypt_invalid_key(self):
        self.assertRaises(ValueError, encrypt, "hello", 35)

    def test_encrypt_with_key(self):
        encrypted = encrypt("Hello World", 2)
        self.assertEquals(encrypted, "jgnnq yqtnf")

    def test_encrypt_special_character(self):
        encrypted = encrypt("Hello World!", 2)
        self.assertEquals(encrypted, "jgnnq yqtnf!")

    def test_encrypt_empty(self):
        encrypted = encrypt("", 1)
        self.assertEqual(encrypted, "")

    def test_decrypt_with_key(self):
        decrypted = decrypt("jgnnq yqtnf", 2)
        self.assertEquals(decrypted, "hello world")

    def test_decrypt_special_character(self):
        decrypted = decrypt("#jgnnq yqtnf", 2)
        self.assertEquals(decrypted, "#hello world")
