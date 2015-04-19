__author__ = 'kskrishnasangeeth'

import string


class Error(Exception):
    pass


class WrongKey(Error):
    """ class created for throwing Exception in the
        event of wrong key being supplied.

    Attributes:
        msg (str): Explanation on why key is not allowed.
        key (int): Key that is supplied.

    Args:
        msg (str): Explanation on why key is not allowed.
        key (int): Key that is supplied.

   """
    def __init__(self, msg, key):
        self.msg = msg
        self.key = key


class NoKeyGiven(Error):
    """ class created for throwing Exception in the
        event of no key being supplied.

    Attributes:
        msg (str): Message to provide key for encryption.

    Args:
        msg (str): Message to provide key for encryption.

    """
    def __init__(self, msg):
        self.msg = msg


def cipher_helper(message, key):
    """Function for modularising and removing some of the repeated code.

    Args:
        message (str): Message that is supplied for encryption/decryption.
        key (int): Key used for encryption/decryption.

    Returns:
        message (str): Message in lowercase.

    """
    if key is None:
        raise NoKeyGiven("Key is needed for Encryption.")

    if key <= 0 or key >= 27:
        raise WrongKey("Key Value should be between 0 and 26. Got Key as", key)

    return message.lower()


def encrypt(message, key=None):
    """Returns the encrypted message for the string passed as argument.

    Uses a random key for generating the cipher text

    Args:
        message (str): The message to be encrypted.
        key (int): The key based on which encryption is performed.

    Returns:
        str: the encrypted message.

    """
    cipher_text = ""
    msg = cipher_helper(message, key)
    for each_char in msg:
        char_pos = string.lowercase.find(each_char)
        if char_pos == -1:
            cipher_text += each_char
            continue
        else:
            char_pos = (char_pos + key) % 26
            cipher_text += string.lowercase[char_pos]
    return cipher_text


def decrypt(message, key):
    """Returns the actual message which was encrypted
       with caesar cipher using Key.

    Args:
        message (str): The message to be decrypted.
        key (int): The key based on which decryption
                   is performed.

    Returns:
        str:  The message which was decrypted.

    """
    decrypt_text = ""
    msg = cipher_helper(message, key)
    for each_char in msg:
        char_pos = string.lowercase.find(each_char)
        if char_pos == -1:
            decrypt_text += each_char
            continue
        else:
            char_pos = (char_pos - key) % 26
            decrypt_text += string.lowercase[char_pos]
    return decrypt_text
