# -*- coding: utf-8 -*-
"""Transposition cipher implementation

Provides functions to encrypt/decrypt a message by transpose ciphering it.

"""


def encrypt(key, message):
    '''Returns encrypted message.

    Args :
        key(int): key for transposition cipher encryption.
        message(string):Message to be encrypted using transposition
          cipher encryption.
    Returns:
        String : Encrypted message
    Raises:
        ValueError: When the key is greater than half
        of the message size,this exception is raised.
    '''
    message_size = len(message)
    # the transposition cipher key is limited to half the length of the
    # message it is used to encrypt
    if key > message_size//2:
        raise ValueError('Key is limited to half the length of message')
    else:
        encrypted_message = [''] * key
        letter_index = 0
        while letter_index < message_size:
            column_index = 0
            while column_index < key and letter_index < message_size:
                encrypted_message[column_index] += message[letter_index]
                letter_index += 1
                column_index += 1
        encrypted_message = ''.join(encrypted_message)
        return encrypted_message