import string
class EnglishChecker():
    """This class serves the purpose of checking if a statement is English or not.
       Two filter methods accomplish this by ensuring:
        1. At least 85% of the message comprises of english alphabets
        2. At least 25% of the words in the sentence are contained in
           the dictionary file, an exhaustive list of english words
    """
    
    def __init__(self):
       
        self.LETTERS_AND_SPACE = string.ascii_letters + string.whitespace
        f = open('/home/travis/build/Anupama-Github/libcipher/libcipher/dictionary.txt')
        #f = open('/home/travis/build/Chennaipy/libcipher/libcipher')
        self.english_words = {}
        for word in f.read().split('\n'):
            self.englishWords[word] = None
        f.close()
        self.ENGLISH_WORDS = self.english_words

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

    def removeNonLetters(self, message):
        lettersOnly = []
        for symbol in message:
            if symbol in self.LETTERS_AND_SPACE:
                lettersOnly.append(symbol)
        return ''.join(lettersOnly)

    def is_english(self, message, word_percentage=25, letterPercentage=85):
        """Checks to see if given text is in English and 
           returns the result.
        Args:
        self (object): Default argument in methods of a class.
            It represents an object of this class
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
        wordsMatch = self.getEnglishCount(message) * 100 >= wordPercentage
        numLetters = len(self.removeNonLetters(message))
        messageLettersPercentage = float(numLetters) / len(message) * 100
        lettersMatch = messageLettersPercentage >= letterPercentage
        return wordsMatch and lettersMatch 
