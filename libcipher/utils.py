
class EnglishChecker():
    """This class serves the purpose of checking if a statement is English or not.
       Two filter methods accomplish this by ensuring:
        1. At least 85% of the message comprises of english alphabets
        2. At least 25% of the words in the sentence are contained in
           the dictionary file, an exhaustive list of english words
    """
    def __init__(self):
        self.UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower = self.UPPERLETTERS.lower()
        self.LETTERS_AND_SPACE = self.UPPERLETTERS + lower + ' \t\n'
        f = open('/home/mer/dictionary.txt')
        self.englishWords = {}
        for word in f.read().split('\n'):
            self.englishWords[word] = None
        f.close()
        self.ENGLISH_WORDS = self.englishWords

    def getEnglishCount(self, message):
        message = message.upper()
        message = self.removeNonLetters(message)
        possibleWords = message.split()
        if possibleWords == []:
            return 0.0  # no words at all, so return 0.0
        matches = 0
        for word in possibleWords:
            if word in self.ENGLISH_WORDS:
                matches += 1
        return float(matches) / len(possibleWords)

    def removeNonLetters(self, message):
        lettersOnly = []
        for symbol in message:
            if symbol in self.LETTERS_AND_SPACE:
                lettersOnly.append(symbol)
        return ''.join(lettersOnly)

    def is_english(self, message, wordPercentage=25, letterPercentage=85):
        """Takes input, returns True for English input, else returns False"""
        if len(message) == 0:
            return False
        wordsMatch = self.getEnglishCount(message) * 100 >= wordPercentage
        numLetters = len(self.removeNonLetters(message))
        messageLettersPercentage = float(numLetters) / len(message) * 100
        lettersMatch = messageLettersPercentage >= letterPercentage
        return wordsMatch and lettersMatch
