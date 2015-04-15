__author__ = 'kskrishnasangeeth'

import random
import sys


def encrypt(message, key=None):
    """Returns the encrypted messsage for the string passed as argument.

    Uses a random key for generating the cipher text

    Args:
        message (str) : The message to be encrypted.
        key (int) : The key based on which encryption is performed. Is optional value.

    Return:
        str: the encrypted message """

    if key is None:
        key = random.randint(1, 25)

    if key <= 0 or key >= 27:
        print('Key should be having value between 1 and 26 ')
        sys.exit(0)
    cipher_text = ""
    message = message.lower()
    for each_char in message:
        if each_char == ' ' or not each_char.isalpha():
            cipher_text += each_char
            continue
        else:
            changed_char = chr(ord(each_char) + key)
            if ord(changed_char) > ord('z'):
                changed_char = chr(ord(each_char) + (key - 26))
            cipher_text += changed_char
    return cipher_text


def decrypt(message, key):
    """Returns the actual message which was encrypted with caesar cipher using Key.

    Args:
        message (str) : The message to be decrypted.
        key (int)     : The key based on which decryption is performed.

    Return:
        str : The message which was decrypted."""

    if key <= 0 or key >= 27:
        print('Key should be having value between 1 and 26')
        sys.exit(0)
    decrypt_text = ""
    message = message.lower()
    for each_char in message:
        if each_char == ' ' or not each_char.isalpha():
            decrypt_text += each_char
            continue
        else:
            changed_char = chr(ord(each_char) - key)
            if ord(changed_char) < ord('a'):
                changed_char = chr(ord(each_char)  + (26 - key))
            decrypt_text += changed_char
    return decrypt_text

