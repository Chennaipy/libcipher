"""Transposition cipher implementation

Provides functions to encrypt / decrypt a message by changing the
character position of plain text.

>>> decrypt(8, 'Cenoonommstmme oo snnio. s s c')
'Common sense is not so common.'

"""
from __future__ import division
import math

# The Transposition decrypt function will simulate the columns and
# rows of the grid that the plain text is written on by using a list of
# strings. No of Columns is calculated by (length of the text)/key.
# key value is consider as no of rows.


def decrypt(key, message):
    """Returns message decrypted using Transposition Cipher

    Args:
      key (int): Integer indicating Encryption key to decrypt message.
      message (str): An encrypted string

    Returns:
      str: A decrypted message
    """

    num_of_columns = int(math.ceil(len(message) / key))
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)

    plaintext = [''] * num_of_columns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == num_of_columns or
             col == num_of_columns - 1 and
             row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)
