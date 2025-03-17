"""
This file has all the unit tests for file_handler.py

Classes and their functions
    TestLocateFolder - tests different cases of the locate_folder function
        test_file_found_single - checks if the test file is found
        test_file_not_found - test that a file is not found
        test_multiple_files_found - tests if a file is found if there is more than one file in a folder
    TestDirectoryPathFormat - tests different cases of the directory_path_format function
        test_valid_paths - tests a variety of correct paths
        test_invalid_paths - tests a variety of paths with prohibited characters
        test_empty_string - test edge case of an empty string
        test_no_backslashes - returns True if the function detects that there are no backslashes directory_path
        test_invalid_drive_letter - returns True if the function detects that there is no driver letter
    TestFilenameFormat - tests different cases of the filename_format function
        test_valid_pdf_filename_lowercase - tests a file that ends with .pdf
        test_valid_pdf_filename_uppercase -  tests a file that ends with .PDF
        test_valid_pdf_filename_mixed_case - tests a mixed cased version of ".pdf"
        test_invalid_filename_no_extension - tests a string with no extension
        test_invalid_filename_wrong_extension - tests a string with the wrong extension
        test_invalid_filename_multiple_dots -  tests a string with multiple extensions
        test_invalid_filename_empty_string - tests an empty string
        test_invalid_filename_only_extension - test a string that only has an extension
        test_invalid_filename_with_spaces - test a string that contains a backspace
        test_invalid_filename_with_special_characters - test a string that contains a special character
    TestDeterminePDFBytes - checks if a file is a PDF by looking for a pattern in the file
        test_valid_pdf_file - test a valid file
        test_invalid_pdf_file - test an invalid file
        test_empty_file - tests an empty file
        test_pdf_without_percent - tests an incorrect PDF pattern
    TestWriteIntoFile - tests that the 3 strings are in a file
        test_write_into_file - test a file has all the strings with their correct sizes
        test_write_nothing_into_file - test to check if the function writes an empty string for the as the
        binary_encrypted_data in the string
    TestGet_values - tests that the 3 strings are returned by a function
        test_read_from_file - test a file returns all the strings with their correct sizes
"""

import os
import unittest
from unittest.mock import mock_open, patch
from file_handler import *


class TestLocateFolder(unittest.TestCase):
    @unittest.skip("")
    def test_file_found_single(self):
        """
        Test that the function returns the correct path when the file is found.
        """
        test_directory = "/tmp"
        test_filename = "target.txt"
        expected_path = os.path.join(test_directory, test_filename)

        # mocked directory structure
        # /C:\\tmp
        #   └── /subdir
        #        ├── target.txt
        #        ├── other.txt
        with patch('os.walk', return_value=[(test_directory, ['subdir'], [test_filename, "other.txt"])]):
            # When locate_folder is called, it will use the patched os.walk.
            result = locate_folder(test_directory, test_filename)
            # Assert that the returned path matches the expected path.
            self.assertEqual(result, expected_path)


    @unittest.skip("")
    def test_file_not_found(self):
        """
        Test that the function returns None when the file is not found.
        """
        test_directory = "/tmp"
        test_filename = "target.txt"

        # mocked directory structure
        # /C:\\tmp
        #   └── /subdir
        #        ├── other.txt
        with patch('os.walk', return_value=[(test_directory, ['subdir'], ["other.txt"])]):
            result = locate_folder(test_directory, test_filename)   # Calls locate_folder with os.walk patched.
            self.assertIsNone(result)    # Checks whether the file is found


    @unittest.skip("")
    def test_multiple_files_found(self):
        """
        Tests that the function returns the first occurrence of a file.
        """
        test_directory = "C:\\tmp"
        test_filename = "target.txt"
        expected_path = 'C:\\tmp\\target.txt'

        # mocked directory structure
        # /C:\\tmp
        #   └── target.txt
        #   ├── other.txt
        with patch ('os.walk', return_value=[(test_directory, [], [test_filename, "other.txt"])]):
            result = locate_folder(test_directory, test_filename)

            self.assertEqual(result, expected_path)     # Assert if the function found the first occurrence of a file.




class TestDirectoryPathFormat(unittest.TestCase):
    @unittest.skip("")
    def test_valid_paths(self):
        """This function test a variety of valid file paths"""
        self.assertTrue(directory_path_format("C:\\Users\\Name\\Documents"))
        self.assertTrue(directory_path_format("D:\\Downloads\\MyFile"))
        self.assertTrue(directory_path_format("E:\\Folder\\Subfolder\\"))
        self.assertTrue(directory_path_format("F:\\Folder\\Subfolder\\File.txt"))

    @unittest.skip("")
    def test_invalid_paths(self):
        """This function test a variety of invalid file paths"""
        self.assertFalse(directory_path_format("C:Users\\Name\\Documents"))  # No backslash after the drive letter
        self.assertFalse(directory_path_format("C:"))
        self.assertFalse(directory_path_format("C:\\Folder\\Invalid<>Name"))
        self.assertFalse(directory_path_format("C:\\Folder\\Invalid|Name"))
        self.assertFalse(directory_path_format("C:\\Folder\\Invalid*Name"))
        self.assertFalse(directory_path_format("C:\\Folder\\Invalid?Name"))
        self.assertFalse(directory_path_format("C:\\Folder\\Invalid\"Name"))
        self.assertFalse(directory_path_format("C:\\Folder\\Invalid:Name"))
        self.assertFalse(directory_path_format("C:\\Folder\\Invalid/Name"))
        self.assertFalse(directory_path_format("C:\\Folder\\Invalid:Name"))

    @unittest.skip("")
    def test_empty_string(self):
        """Tests the function returns False when its parameter is an empty string"""
        self.assertFalse(directory_path_format(""))

    @unittest.skip("")
    def test_no_backslashes(self):
        """ tests that a correct error message is printed in the commandline specifying that there are no backlashes"""
        self.assertFalse(directory_path_format("C:FolderName"))

    @unittest.skip("")
    def test_invalid_drive_letter(self):
        """ tests that a correct error message is printed in the commandline specifying that the driver character is
        wrong"""
        self.assertFalse(directory_path_format("1:\\Folder\\Name"))  # Wrong drive character




class TestFilenameFormat(unittest.TestCase):
    @unittest.skip("")
    def test_valid_pdf_filename_lowercase(self):
        """returns True if the .pdf is a valid extension"""
        self.assertTrue(filename_format("document.pdf"))

    @unittest.skip("")
    def test_valid_pdf_filename_uppercase(self):
        """returns True if the .PDF is a valid extension"""
        self.assertTrue(filename_format("report.PDF"))

    @unittest.skip("")
    def test_valid_pdf_filename_mixed_case(self):
        """returns True if a mixed case version '.pdf' is a not a valid extension"""
        self.assertFalse(filename_format("Presentation.PdF"))

    @unittest.skip("")
    def test_invalid_filename_no_extension(self):
        """returns True if the file can detect that the string has no extension"""
        self.assertFalse(filename_format("document"))

    @unittest.skip("")
    def test_invalid_filename_wrong_extension(self):
        """returns True if the file can detect that the string has the wrong extension"""
        self.assertFalse(filename_format("image.png"))

    @unittest.skip("")
    def test_invalid_filename_multiple_dots(self):
        """returns True if the file can detect that the string has too many extensions"""
        self.assertFalse(filename_format("archive.tar.gz"))

    @unittest.skip("")
    def test_invalid_filename_empty_string(self):
        """returns True if the file can detect that the string is empty"""
        self.assertFalse(filename_format(""))

    @unittest.skip("")
    def test_invalid_filename_only_extension(self):
        """returns True if the file can detect that the string has no name"""
        self.assertFalse(filename_format(".pdf"))

    @unittest.skip("")
    def test_invalid_filename_with_spaces(self):
        """returns True if the file can detect that the string has a backspace"""
        self.assertTrue(filename_format("my document.pdf"))

    @unittest.skip("")    
    def test_invalid_filename_with_special_characters(self):
        """returns True if the file can detect that the string has a prohibited character"""
        self.assertTrue(filename_format("file@name.pdf"))


class TestDeterminePDFBytes(unittest.TestCase):
    @unittest.skip("")
    @patch("builtins.open", new_callable=mock_open, read_data=b'%PDF-1.4\n')
    def test_valid_pdf_file(self, mock_file):
        """ Tests that the file has a pattern that determines that it is a PDF"""
        result = determine_PDF_bytes("valid_file.pdf")
        self.assertTrue(result)
        mock_file.assert_called_once_with("valid_file.pdf", "rb")

    @unittest.skip("")
    @patch("builtins.open", new_callable=mock_open, read_data=b'not a pdf')
    def test_invalid_pdf_file(self, mock_file):
        """ Tests that the file does not have the pattern that determines that it is a PDF"""
        result = determine_PDF_bytes("invalid_file.txt")
        self.assertFalse(result)
        mock_file.assert_called_once_with("invalid_file.txt", "rb")

    @unittest.skip("")
    @patch("builtins.open", new_callable=mock_open, read_data=b'')
    def test_empty_file(self, mock_file):
        """tests that an empty file returns False without side effects"""
        result = determine_PDF_bytes("empty_file.pdf")
        self.assertFalse(result)
        mock_file.assert_called_once_with("empty_file.pdf", "rb")

    @unittest.skip("")
    @patch("builtins.open", new_callable=mock_open, read_data=b'PDF-1.4\n')
    def test_pdf_without_percent(self, mock_file):
        """tests that function returns False without side effects when the pattern is incorrect"""
        result = determine_PDF_bytes("no_percent_file.pdf")
        self.assertFalse(result)
        mock_file.assert_called_once_with("no_percent_file.pdf", "rb")



class TestWriteIntoFile(unittest.TestCase):
    @unittest.skip("")
    @patch("builtins.open", new_callable=mock_open)
    def test_write_into_file(self, mock_file):
        """test the correct length substrings in a string"""
        # Sample data
        binary_encrypted_data = b"encrypted_data"
        key = b"random_key_32_bytes_long!"  # 32 bytes for Blowfish
        initialization_vector = b"iv_8_bytes"  # 8 bytes for Blowfish

        write_into_file(binary_encrypted_data, key, initialization_vector)

        # Check that the file was opened in right mode
        mock_file.assert_called_once_with("encrypted_file.bin", 'wb')

        # Check what data was written into the file
        mock_file().write.assert_any_call(binary_encrypted_data)
        mock_file().write.assert_any_call(key)
        mock_file().write.assert_any_call(initialization_vector)

        # Check  the total number of write calls
        self.assertEqual(mock_file().write.call_count, 3)

    @unittest.skip("")
    @patch("builtins.open", new_callable=mock_open)
    def test_write_nothing_into_file(self, mock_file):
        """test a string where it only has two substrings"""
        # Sample data
        binary_encrypted_data = b""
        key = b"random_key_32_bytes_long!"  # 32 bytes for Blowfish
        initialization_vector = b"iv_8_bytes"  # 8 bytes for Blowfish

        write_into_file(binary_encrypted_data, key, initialization_vector)

        # Check that the file was opened in right mode
        mock_file.assert_called_once_with("encrypted_file.bin", 'wb')

        # Check what data was written into the file
        mock_file().write.assert_any_call(binary_encrypted_data)
        mock_file().write.assert_any_call(key)
        mock_file().write.assert_any_call(initialization_vector)

        # Check  the total number of write calls
        self.assertEqual(mock_file().write.call_count, 3)




class TestGet_values(unittest.TestCase):

    @unittest.skip("")
    @patch("builtins.open", new_callable=mock_open)
    def test_read_from_file(self, mock_file):
        """test a file returns all the strings with their correct sizes"""
        # Sample data
        binary_encrypted_data = b"Phasellus eget orci a orci mollis malesuada. Ut tempor bibendum tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam erat volutpat. Cras et nulla tristique, pellentesque lacus eu, vestibulum urna. Vivamus semper risus sed justo faucibus ultrices. Phasellus in odio diam. Mauris commodo eros et sem dapibus condimentum. Ut."
        key = b"random_key_32_bytes_long!"  # 32 bytes for Blowfish
        initialization_vector = b"iv_8_bytes"  # 8 bytes for Blowfish

        # Prepare the mock file content
        mock_file_content = (
            binary_encrypted_data +
            key +
            initialization_vector
        )

        # Simulated file reading
        mock_file().read.return_value = mock_file_content


        result_data, result_key, result_iv = get_values()

        # Check that the returned values are correct
        self.assertEqual(result_data, binary_encrypted_data)
        self.assertEqual(result_key, key)
        self.assertEqual(result_iv, initialization_vector)




if __name__ == '__main__':
    unittest.main()