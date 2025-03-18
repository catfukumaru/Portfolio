import unittest
from unittest.mock import mock_open, patch, call
from file_handler import *


class MyTestFileHandler(unittest.TestCase):
    @unittest.skip("")
    def test_correct_input(self):
        sample_dir_path = "C:\\Users"
        sample_file = "document.pdf"
        expected_path = os.path.join(sample_dir_path, sample_file)

        self.assertTrue(directory_path_format(sample_dir_path) and filename_format(sample_file))

        if directory_path_format(sample_dir_path) and filename_format(sample_file):
            # if the directory path and the file are in the correct format then return the full path of the file

            # mocked directory structure
            # /C:\\Users
            #   ├── document.pdf
            #   ├── other.txt

            with patch('os.walk', return_value=[(sample_dir_path, [], [sample_file, "other.txt"])]):
                # When locate_folder is called, it will use the patched os.walk.
                result = locate_folder(sample_dir_path, sample_file)
                # Assert that the returned path matches the expected path.
                self.assertEqual(result, expected_path)

    @unittest.skip("")
    def test_correct_input_with_subdirectory(self):
        sample_dir_path = "C:\\Users"
        sample_file = "document.pdf"
        expected_path = os.path.join(sample_dir_path+'\\subdir', sample_file)

        self.assertTrue(directory_path_format(sample_dir_path) and filename_format(sample_file))

        if directory_path_format(sample_dir_path) and filename_format(sample_file):
            # if the directory path and the file are in the correct format then return the full path of the file

            # mocked directory structure
            # /C:\\Users
            #   └── \subdir
                #   ├── document.pdf
                #   ├── other.txt

            with patch('os.walk', return_value=[(sample_dir_path, ['subdir'], []),
                                                (sample_dir_path + '\\subdir', [], [sample_file, 'other.txt'])]):
                # When locate_folder is called, it will use the patched os.walk.
                result = locate_folder(sample_dir_path, sample_file)
                # Assert that the returned path matches the expected path.
                self.assertEqual(result, expected_path)

    @unittest.skip("")
    def test_wrong_dir_path(self):
        sample_dir_path = "C:\\\\Users"
        sample_file = "document.pdf"

        self.assertFalse(directory_path_format(sample_dir_path) and filename_format(sample_file))

    @unittest.skip("")
    def test_wrong_file(self):
        sample_dir_path = "C:\\Users"
        sample_file = "document.docx"

        self.assertFalse(directory_path_format(sample_dir_path) and filename_format(sample_file))

    @patch("builtins.open", new_callable=mock_open)
    def test_write_into_file_and_get_values(self, mock_file):
        """test the correct length substrings in a string"""
        # Sample data
        binary_encrypted_data = b"encrypted_data"
        key = os.urandom(32)  # 32 bytes for Blowfish
        initialization_vector = os.urandom(8) # 8 bytes for Blowfish


        # Call the function
        write_into_file(binary_encrypted_data, key, initialization_vector)

        # Check that the file was opened in right mode
        mock_file.assert_called_once_with("encrypted_file.bin", 'wb')

        # Check what data was written into the file
        mock_file().write.assert_any_call(binary_encrypted_data)
        mock_file().write.assert_any_call(key)
        mock_file().write.assert_any_call(initialization_vector)

        #mock's return the test data when read
        mock_file().read.return_value = binary_encrypted_data+key+initialization_vector

        # Call the function to read data
        test_binary_encrypted_data, test_key, test_initialization_vector = get_values()

        # Check that the file was opened in right mode
        mock_file.assert_called_with("encrypted_file.bin", 'rb')

        # Check that the returned values are correct
        self.assertEqual(test_binary_encrypted_data, binary_encrypted_data)
        # self.assertEqual(test_key, key)
        # self.assertEqual(test_initialization_vector, initialization_vector)




if __name__ == '__main__':
    unittest.main()
