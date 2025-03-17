"""
This file has the encryption and decryption functions for the Blowfish algorithm

functions
    encryption_Blowfish: encrypts data with the Blowfish algorithm
    decryption_Blowfish: decrypts data with the Blowfish algorithm
"""

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding # used to make the binary text match the block sized for the mode


def encryption_Blowfish(binary_text):
    """takes a binary string and encrypt the data using the Blowfish algorithm

    param:
        binary_text = binary string
    returns:
        cipher_text, key, initialization_vector = a tuple with the binary strings
    """

    # changes the size of the binary_text to make it fit the requirements of Blowfish
    padder = padding.PKCS7(64).padder()
    padded_data = padder.update(binary_text)
    padded_data += padder.finalize()    #.finalize() handles the padded data and return the rest of the data.

    key = os.urandom(32) # size of the key
    initialization_vector = os.urandom(8)
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(initialization_vector)) # combines an algorithm with a mode

    #encrypts the data
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(padded_data)
    return cipher_text, key, initialization_vector




def decryption_Blowfish(cipher_text_and_key_and_initialization_vector):
    """takes a binary string and encrypt the data using the Blowfish algorithm

        param:
            cipher_text_and_key_and_initialization_vector = a tuple with the binary strings
        returns:
            message = binary string
    """

    cipher_text, key, initialization_vector = cipher_text_and_key_and_initialization_vector

    # decrypts the string
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(initialization_vector))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(cipher_text)

    # decrypts the data
    unpadder = padding.PKCS7(64).unpadder()
    message = unpadder.update(padded_data)
    message = message + unpadder.finalize()     # .finalize() handles the unpadded data and returns bytes.

    return message




# used
# https://cryptography.io/en/latest/hazmat/primitives/padding/


