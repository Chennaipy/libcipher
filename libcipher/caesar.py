"""Caesar cipher implementation.

Provides functions to encrypt / decrypt a message using Caesar Cipher.

>>> encrypt("hello world", 5)
'mjqqt btwqi'
>>> decrypt('mjqqt btwqi', 5)
'hello world'
"""

__author__ = 'kskrishnasangeeth'

import string


def __cipher_helper(message, key):
    """Returns encrypted / decrypted text.

    Args:
        message (str): the message to be encrypted / decrypted.
        key (int): the encryption / decryption key.

    Returns:
        message (str): the encrypted / decrypted message.
    """

    cipher_text = ""
    for each_char in message.lower():
        char_pos = string.ascii_lowercase.find(each_char)
        if char_pos == -1:
            cipher_text += each_char
            continue
        else:
            char_pos = (char_pos + key) % 26
            cipher_text += string.ascii_lowercase[char_pos]
    return cipher_text


def encrypt(message, key):
    """Returns the encrypted message.

    The message string that is  passed as argument gets
    encrypted using the key that is supplied.

    Args:
        message (str): the message to be encrypted.
        key (int): the encryption key.

    Returns:
        str: the encrypted message.
    """

    __check_key(key)
    encrypt_text = __cipher_helper(message, key)
    return encrypt_text


def decrypt(message, key):
    """Returns the decrypted message.

    The encoded message that is passed as argument gets
    decrypted using the key provided.

    Args:
        message (str): the message to be decrypted.
        key (int): the decryption key.

    Returns:
        str: the decrypted message.
    """
    
    __check_key(key)
    decrypt_text = __cipher_helper(message, -key)
    return decrypt_text


def __check_key(key):
    """Validate encryption / decryption key.

    Args:
        key (str): the key to be validated
    """
    
    if key <= 0 or key >= 27:
        raise ValueError("Key  should be between 0 and 26. Got Key as", key)
