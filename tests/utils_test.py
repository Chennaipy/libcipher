"""Unit tests for english language checker"""
import unittest
import libcipher.utils as utils

filepath = '/home/travis/build/Chennaipy/libcipher/libcipher/dictionary.txt'

class english_check_testcase(unittest.TestCase):
    
    def test_for_english(self):
        x = utils.EnglishChecker(filepath)
        self.assertTrue(x.is_english("Mary had a little lamb"))

    def test_for_non_english(self):
        x = utils.EnglishChecker(filepath)
        self.assertFalse(x.is_english("Mary avait un petit agneau"))

    def test_for_no_letters(self):
        x = utils.EnglishChecker(filepath)
        self.assertFalse(x.is_english("222 #@#!#<:"))

if __name__ == '__main__':
    unittest.main()
