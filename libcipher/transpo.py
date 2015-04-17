"""Transposition cipher implementation

Provides functions to encrypt / decrypt a message by changing the
character position of plain text.

>> decrypt(8, 'Cenoonommstmme oo snnio. s s c')
'Common sense is not so common.'

"""
import math


def decrypt(key, message):
    """Return decrypted message using Transposition Cipher

    The Transposition decrypt function will simulate the columns and
    rows of the grid that the plain text is written on by using a list of
    strings. No of Columns is calculated by (length of the text)/key.
    key value is consider as no of rows.

    Args:
         key (int): Encryption key to decrypt message
         message (str): Encrypted message

    Returns:
        Decrypted message as string.

    """

    numOfColumns = int(math.ceil(len(message) / key))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numOfColumns) or \
        (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)
