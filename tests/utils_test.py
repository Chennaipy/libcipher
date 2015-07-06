"""Unit tests for english language checker."""

from libcipher import utils
import io
import sys
import unittest

#
# Based on http://python3porting.com/noconv.html
#
if sys.version_info < (3,):
	import codecs
	def u(x):
		return codecs.unicode_escape_decode(x)[0]
else:
	def u(x):
		return x


def get_marys_dictionary():
	english_words = ["had", "a", "little", "lamb"]
	dict_file = io.StringIO(u('\n').join(english_words))
	return dict_file


class EnglishCheckTestCase(unittest.TestCase):

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
