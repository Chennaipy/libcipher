"""Unit tests for english language checker"""
from libcipher import utils as utils
import io
import sys
import unittest


def get_marys_dictionary():
        english_words = ["had", "a", "little", "lamb"]
        text = str("\n".join(english_words))
        if sys.version < '3':
            dict_file = io.StringIO(unicode('\n').join(english_words))
        else:
            dict_file = io.StringIO("\n".join(english_words))
        return dict_file


class english_check_testcase(unittest.TestCase):

        def test_for_english(self):
            dict_file = get_marys_dictionary()
            checker = utils.EnglishChecker(dict_file)
            dict_file.close()
            self.assertTrue(checker.is_english("Mary had a little lamb"))

        def test_for_non_english(self):
            dict_file = get_marys_dictionary()
            checker = utils.EnglishChecker(dict_file)
            dict_file.close()
            self.assertFalse(checker.is_english("Mary avait un petit agneau"))

        def test_for_no_letters(self):
            dict_file = get_marys_dictionary()
            checker = utils.EnglishChecker(dict_file)
            dict_file.close()
            self.assertFalse(checker.is_english("222 #@#!#<:"))


if __name__ == '__main__':
    unittest.main()
