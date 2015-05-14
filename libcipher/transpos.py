# -*- coding: utf-8 -*-
"""Transposition cipher implementation

Provides functions to encrypt/decrypt a message by transpose ciphering it.

"""


class Error(Exception):
    pass


class InvalidKeySizeException(Error):
    '''Invalid key size exception

    When keysize is greater than half of size of message size,this
    exception is thrown with description indicating keysize and message size.

    Attributes:
        keysize (int): Size of Key
        messagesize(int): Size of message

    Args:
        keysize (int): Size of Key
        messagesize(int): Size of message
    '''

    def __init__(self, keysize, messagesize):
        self.keysize = keysize
        self.messagesize = messagesize

    def __str__(self):
        return(
            "Cipher key is limited to half the length of the message" +
            " size.\nKey Size is " + repr(self.keysize) +
            " and Message Size is " + repr(self.messagesize))


def encrypt(keysize, message):
    '''Transpose Cipher Encrypt function.

    Args :
        keysize(int): Keysize for transposition cipher encryption.
        message(string):Message to be encrypted using transposition
          cipher encryption.
    Returns:
        String : For valid message and keysize,encrypetd message with '|'
          at end is returned.
          When message is '','|' is alone returned as encrypted message.

    Raises:
        InvalidKeySizeException: When the keysize is greater than half
        of the message size,this exception is raised.
    '''
    message_size = len(message)
    # the transposition cipher key is limited to half the length of the
    # message it is used to encrypt
    if keysize <= message_size//2:
        encrypted_message = keysize * ['']
        letter_index = 0
        while letter_index < message_size:
            column_index = 0
            while column_index < keysize and letter_index < message_size:
                encrypted_message[column_index] += message[letter_index]
                letter_index += 1
                column_index += 1
        encrypted_message = ''.join(encrypted_message)+'|'
        return encrypted_message
    else:
        if message_size == 0:
            encrypted_message = '|'
            return encrypted_message
        else:
            # Raise an exception indicating invalid KeySize for
            # non-empty message
            raise InvalidKeySizeException(keysize, message_size)
            return ''
