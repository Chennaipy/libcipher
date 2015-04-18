""" 

Transposition cipher implementation.

Provides functions to encrypt / decrypt a message by transpose ciphering it.

Encryption needs a key(a number).

"""


def encrypt(keysize,message):
    '''
    Args :
        Transposition Cipher Key Size,Message
    Returns:
        message encrypted using transposition cipher
    '''
    message_size = len(message)
    #the transposition cipher’s key is limited to half the length of the 
    #message it is used to encrypt
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
        #print('Key Size is Invalid')       
        return '|'