# -*- coding: utf-8 -*-
"""Transposition cipher implementation.

Provides functions to encrypt/decrypt a message by transpose ciphering it.

>>> encrypt(8, 'Common sense is not so common.')
'Cenoonommstmme oo snnio. s s c'
>>> decrypt(8, 'Cenoonommstmme oo snnio. s s c')
'Common sense is not so common.'
"""

from __future__ import division
import math


def encrypt(key, message):
    '''Returns the encrypted message.

    Args:
        key(int): the encryption key.
        message(string): message to be encrypted.
          
    Returns:
        string: the encrypted message
        
    Raises:
        ValueError: When the key is greater than half of the message size
    '''
    message_size = len(message)
    # the transposition cipher key is limited to half the length of the
    # message it is used to encrypt
    if key > message_size//2:
        raise ValueError('Key is limited to half the length of message')
    else:
        encrypted_message = [''] * key
        for col in range(key):
            pointer = col
            while pointer < message_size:
                encrypted_message[col] += message[pointer]
                pointer += key
        encrypted_message = ''.join(encrypted_message)
        return encrypted_message


# The Transposition decrypt function will simulate the columns and
# rows of the grid that the plain text is written on by using a list of
# strings. No of Columns is calculated by (length of the text)/key.
# key value is consider as no of rows.


def decrypt(key, message):
    """Returns the decrypted message.

    Args:
      key (int): decryption key
      message (str): the encrypted string

    Returns:
      str: the decrypted message.
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
