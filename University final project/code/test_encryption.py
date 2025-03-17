"""
This file has all the unit tests for file_handler.py

Classes and their functions
    TestEncryptionBlowfish - test the function that encrypts the data
        test_encryption_with_small_binary - test the function with the binary_text containing a short length binary string
        test_encryption_with_empty_binary - test the function with the binary_text containing an empty binary string
        test_encryption_with_large_binary - test the function with the binary_text containing a long length binary string
        test_encryption_with_non_ascii_binary - test the function with the binary_text containing a binary string with non-ascii characters
    TestEncryptionDecryptionBlowfish - test the function that decrypts the data
        setUp - sets up the encrypted strings to be used before each test
        test_decryption - tests that the original message and the decrypted message are the same
        test_decryption_with_empty_string - tests the function when there is no message
        test_decryption_with_non_ascii - test the function with the binary_text containing a binary string with non-ascii characters

"""

import unittest
from encryption import *


class TestEncryptionBlowfish(unittest.TestCase):
    """tests that the function against a variety of binary data as input"""
    @unittest.skip("")
    def test_encryption_with_small_binary(self):
        binary_text = b"Hello, World!"
        cipher_text, key, iv = encryption_Blowfish(binary_text)

        # Checks that the cipher text is not empty
        self.assertGreater(len(cipher_text), 0)
        # Checks that the key is 32 bytes long
        self.assertEqual(len(key), 32)
        # Check that the IV is 8 bytes long
        self.assertEqual(len(iv), 8)

    @unittest.skip("")
    def test_encryption_with_empty_binary(self):
        binary_text = b""
        cipher_text, key, iv = encryption_Blowfish(binary_text)

        # Checks that the cipher text is not empty
        self.assertGreater(len(cipher_text), 0)
        # Checks that the key is 32 bytes long
        self.assertEqual(len(key), 32)
        # Check that the IV is 8 bytes long
        self.assertEqual(len(iv), 8)

    @unittest.skip("")
    def test_encryption_with_large_binary(self):
        binary_text = os.urandom(1024)  # 1 KB of random data
        cipher_text, key, iv = encryption_Blowfish(binary_text)

        # Checks that the cipher text is not empty
        self.assertGreater(len(cipher_text), 0)
        # Checks that the key is 32 bytes long
        self.assertEqual(len(key), 32)
        # Check that the IV is 8 bytes long
        self.assertEqual(len(iv), 8)

    @unittest.skip("")
    def test_encryption_with_non_ascii_binary(self):
        binary_text = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
        cipher_text, key, iv = encryption_Blowfish(binary_text)

        # Check that the cipher text is not empty
        self.assertGreater(len(cipher_text), 0)
        # Checks that the key is 32 bytes long
        self.assertEqual(len(key), 32)
        # Check that the IV is 8 bytes long
        self.assertEqual(len(iv), 8)



class TestEncryptionDecryptionBlowfish(unittest.TestCase):
    @unittest.skip("")
    def setUp(self):
        # Sample data
        self.binary_text = b"Hello, World!"
        self.padder = padding.PKCS7(64).padder()
        padded_data = self.padder.update(self.binary_text) + self.padder.finalize()

        # Generates a key and IV
        self.key = os.urandom(32)
        self.initialization_vector = os.urandom(8)

        # Encrypts the data
        cipher = Cipher(algorithms.Blowfish(self.key), modes.CBC(self.initialization_vector))
        encryptor = cipher.encryptor()
        self.cipher_text = encryptor.update(padded_data)


    @unittest.skip("")
    def test_decryption(self):
        # Prepare the input for decryption
        input_data = (self.cipher_text, self.key, self.initialization_vector)
        decrypted_message = decryption_Blowfish(input_data)

        # Checks that the decrypted message matches
        self.assertEqual(decrypted_message, self.binary_text)

    @unittest.skip("")
    def test_decryption_with_empty_string(self):
        # Test decryption of an empty string
        empty_text = b""
        padded_empty_data = padding.PKCS7(64).padder().update(empty_text) + padding.PKCS7(64).padder().finalize()

        # Encrypts the empty string
        cipher = Cipher(algorithms.Blowfish(self.key), modes.CBC(self.initialization_vector))
        encryptor = cipher.encryptor()
        cipher_text_empty = encryptor.update(padded_empty_data)

        # decrypts the data
        input_data_empty = (cipher_text_empty, self.key, self.initialization_vector)
        decrypted_empty_message = decryption_Blowfish(input_data_empty)

        # Checks that the decrypted message matches
        self.assertEqual(decrypted_empty_message, empty_text)

    @unittest.skip("")
    def test_decryption_with_non_ascii(self):
        # Test decryption of non-ASCII binary data
        non_ascii_text = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F"
        padded_non_ascii_data = padding.PKCS7(64).padder().update(non_ascii_text) + padding.PKCS7(64).padder().finalize()

        # Encrypts non_ascii_text
        cipher = Cipher(algorithms.Blowfish(self.key), modes.CBC(self.initialization_vector))
        encryptor = cipher.encryptor()
        cipher_text_non_ascii = encryptor.update(padded_non_ascii_data)

        # decrypts the data
        input_data_non_ascii = (cipher_text_non_ascii, self.key, self.initialization_vector)
        decrypted_non_ascii_message = decryption_Blowfish(input_data_non_ascii)

        # Check that the decrypted message matches
        self.assertEqual(decrypted_non_ascii_message, non_ascii_text)




if __name__ == '__main__':
    unittest.main()
