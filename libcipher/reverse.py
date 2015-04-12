"""Reverse cipher implementation.

Provides functions to encrypt / decrypt a message by reversing it.

>>> encrypt('abcd')
'dcba'
>>> encrypt('dcba')
'abcd'
"""

def encrypt(message):
    """Returns message encrypted using reverse cipher.

    Due to the way reverse cipher works, the same function performs
    both encryption and decryption operation.

    Args:
      message (str): The message to be encrypted or decrypted

    Returns:
      str: the encrypted / decrypted message
    """
    return "".join(reversed(message))
