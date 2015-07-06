"""Unit tests for transpostion cipher module."""

import unittest
from libcipher.transpo import decrypt


class TranspositionTestCase(unittest.TestCase):
    def test_decrypt(self):
        decrypted = decrypt(8, 'Cenoonommstmme oo snnio. s s c')
        self.assertEqual(decrypted, 'Common sense is not so common.')
