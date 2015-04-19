"""Transposition cipher implementation

Provides functions to encrypt/decrypt a message by transpose ciphering it.
Encryption needs a key(a number).
"""


class InvalidKeySizeException(Exception):
    def __init__(self, keysize, messagesize):
        self.keysize = keysize
        self.messagesize = messagesize

    def __str__(self):
        return("Cipher key is limited to half the length of the message" + 
        " size.\nKey Size is " + repr(self.keysize) + 
        " and Message Size is " + repr(self.messagesize))


def encrypt(keysize, message):
    '''
    Args :
        Transposition Cipher Key Size,Message
    Returns:
        message encrypted using transposition cipher.'|' is added at to
        indicate end of message.For invalid key size,InvalidKeySizeException
        is thrown.For empty input message,'|' is returned.
    '''
    message_size = len(message)
    # the transposition cipher’s key is limited to half the length of the
    # message it is used to encrypt
    try:
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
    except InvalidKeySizeException as err:
        print(err)
        return ''
print(encrypt(5, 'Hello World'))
print(encrypt(2, ''))
print(encrypt(5, 'Hello'))
