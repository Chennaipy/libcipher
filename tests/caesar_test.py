"""Unit tests for caesar cipher module. """

import unittest
from libcipher.caesar import encrypt, decrypt, NoKeyGiven, WrongKey


class CaesarTestCase(unittest.TestCase):
    def test_encrypt_no_key(self):
        try:
            encrypt("hello")
        except NoKeyGiven as message:
            self.failUnlessEqual(message.args[0], "Key is needed for Encryption.")
        else:
            self.fail("NoKeyGiven Exception not raised")

    def test_encrypt_invalid_key(self):
        try:
            encrypt("hello", 42)
        except WrongKey as message:
            self.failUnlessEqual(message.args[0], "Key Value should be between 0 and 26. Got Key as")
            self.failUnlessEqual(message.args[1], 42)
        else:
            self.fail("WrongKeyGiven Exception not raised")

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
