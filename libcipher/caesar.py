__author__ = 'kskrishnasangeeth'


class Error(Exception):
    pass


class WrongKey(Error):
    """ class created for throwing Exception in the event of wrong key being supplied

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
    """ class created for throwing Exception in the event of no key being supplied

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
        cipher_text (str): the encrypted message.

    """
    cipher_text = ""
    msg = cipher_helper(message, key)
    for each_char in msg:
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
        message (str): The message to be decrypted.
        key (int): The key based on which decryption is performed.

    Returns:
        decrypt_text (str): The message which was decrypted.

    """
    decrypt_text = ""
    msg = cipher_helper(message, key)
    for each_char in msg:
        if each_char == ' ' or not each_char.isalpha():
            decrypt_text += each_char
            continue
        else:
            changed_char = chr(ord(each_char) - key)
            if ord(changed_char) < ord('a'):
                changed_char = chr(ord(each_char) + (26 - key))
            decrypt_text += changed_char
    return decrypt_text