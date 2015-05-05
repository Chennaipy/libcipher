import io
import sys
import string


class EnglishChecker():
    """This class serves the purpose of checking if a statement is
       English or not. Two filter methods accomplish this by ensuring:
        1. At least 85% of the message comprises of english alphabets
        2. At least 25% of the words in the sentence are contained in
           the dictionary file, an exhaustive list of english words
    """

    def __init__(self, filename):
        self.filename = filename
        self.LETTERS_AND_SPACE = string.ascii_letters + string.whitespace
        content = filename.getvalue()
        self.ENGLISH_WORDS = content.upper()

    def get_english_count(self, message):
        message = message.upper()
        message = self.remove_non_letters(message)
        possible_words = message.split()
        if possible_words == []:
            return 0.0  # no words at all, so return 0.0
        matches = 0
        for word in possible_words:
            if word in self.ENGLISH_WORDS:
                matches += 1
        return float(matches) / len(possible_words)

    def remove_non_letters(self, message):
        letters_only = []
        for symbol in message:
            if symbol in self.LETTERS_AND_SPACE:
                letters_only.append(symbol)
        return ''.join(letters_only)

    def is_english(self, message, word_percentage=25, letter_percentage=85):
        """Checks to see if given text is in English and
           returns the result.
        Args:
          message (string): The text input
          word_percentage (int): Indicates the minium
            percentage of English words in the message. The
            default value is 25
          letter_percentage (int): Indicates the minium
            percentage of English alphabets in a word. The
            default value is 85
        Returns:
          bool: True if message is in English, False otherwise.

        """
        if len(message) == 0:
            return False
        words_match = self.get_english_count(message) * 100 >= word_percentage
        num_letters = len(self.remove_non_letters(message))
        message_letters_percentage = float(num_letters) / len(message) * 100
        letters_match = message_letters_percentage >= letter_percentage
        self.filename.close()
        return words_match and letters_match
