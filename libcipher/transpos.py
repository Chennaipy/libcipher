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
        for col in range(key):
            pointer = col
            while pointer < message_size:
                encrypted_message[col] += message[pointer]
                pointer += key
        encrypted_message = ''.join(encrypted_message)
        return encrypted_message