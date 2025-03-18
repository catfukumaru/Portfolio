''' deals with handling the file (finds a file, converts a file, saves and access the data in a file)

functions
    locate_folder: finds the folder the file is in
    directory_path_format: validates the format of the directory path
    filename_format: validates the format of the file string
    determine_PDF_bytes: looks into a file to see if it is a PDF
    write_into_file: writes data into a new file
    get_values: separate the file data, from the values used to dencrypt the file
'''

import os
import re

#
#  File location
#

def locate_folder(directory, filename):
    """
    find the folder in a drive of the computer the program is running on

    param:
        directory = string # it is the full path
        filename = string # it also includes the extension
    returns:
        os.path.join(root,file) = string
    """

    for path, directory, files in os.walk(directory):
        for file in files: # looping through each folder
             if file == filename: #if the file is found
                return os.path.join(path,file) # returns the full path
             else:
                print("Error: The path was not found, check that there are no spelling mistakes.")
    return None

#
#  Format validation
#
def directory_path_format(directory_string):
    """determine whether a file format of the string representing the directory si correct.
            param:
                directory_string = string
            returns:
                boolean value
    """
    pattern = r'^[A-Z]:\\(((?![<>:"/\\|?*]).)+((?<![ .])\\)?)*$'  # pattern for the patth of the folder
    # represents the drive letter (A-Z) followed by a colon:     [A - Z]: .
    # matches the backslash after the drive letter:     \\
    # none of this characters can be in the string <, >, :, ", /, \, |, ?, *:   (?![<>:"/\\|?*]).)+
    # no space characters before the backslash but the backslash can appear more than once:     (?<![ .])\\)?
    # the entire group can appear more than once, i.e: multiple directory levels are allowed:   )*
    # the string needs to match the pattern throughout its length:      $

    if re.match(pattern, directory_string):  # check is the format of the location is correct
        return True
    else:
        # Identifies the part of the path that is wrong
        if not re.match(r'^[A-Z]: ', directory_string):
            print("Error: The path must start with a drive letter followed by a colon.")
        elif not re.search(r'\\+', directory_string):
            print("Error: The path must contain at least one backslash.")
        else:
            # Check for invalid characters in the path
            invalid_chars = re.findall(r'[<>:"/\\|?*]', directory_string)
            if invalid_chars:
                print(f"Error: The path contains at least one of this invalid characters: {', '.join(set(invalid_chars))}.")

    return False

def filename_format(file_string):
    """determine whether a file format of the string representing the filename and its extension are correct.
        param:
            filename_with_extension = string
        returns:
            boolean value
    """
    pattern = r'^[^\t\r\n\\\/<>:"|?*]*[^\t\r\n\\\/<>:"|?*.\s]\.(pdf|PDF)$'
    # from the beginning of the string. this characters must not be in the string:     [^\t\r\n\\\/<>:"|?*].
    # the file must not end with a space character or a period before the file extension:    [^\t\r\n\\\/<>:"|?*.\s]
    # the file is a period and pdf or PDF:    \.(pdf|PDF)$
    if re.match(pattern, file_string):  # check is the format  is correct
        return True
    else:
        print("Error: This program only accepts PDF files")
        return False

def determine_PDF_bytes(filename_with_extension):
    """determine whether a file is a pdf by the first few bytes in the file
        param:
            filename_with_extension = string
        returns:
            boolean value
    """
    with open(filename_with_extension, "rb") as file:
        first_four_bytes= file.read(4)

    if first_four_bytes == b'%PDF':
        return True
    else:
        print("The file selected has the wrong format. Please only use PDF files")
        return False


#
#  Manipulates a file
#


def write_into_file(binary_encrypted_data, key, initialization_vector):
    """writes  binary_encrypted_data, key and  initialization_vector to a file
        param:
            binary_encrypted_data = binary string
            key = binary string
            initialization_vector = binary string

        returns:
            bin_file: BinaryIO = a binary file containing all the parameters in it
    """

    with open("encrypted_file.bin", 'wb') as bin_file:
        bin_file.write(binary_encrypted_data)
        bin_file.write(key)
        bin_file.write(initialization_vector)
    return bin_file

def get_values():
    """get the binary_encrypted_data, key and  initialization_vector from a file
    param:
        file = _io.TextIOWrapper # type given to a file

    returns:
        tuple: It contains the binary_encrypted_data, key and initialization_vector
    """

    KEY_SIZE = 32  # Amount of bytes in the Blowfish key
    IVECTOR_SIZE = 8  # Amount of bytes in the initialization vector

    with open("encrypted_file.bin", 'rb') as bin_file:
        file_content = bin_file.read()
        # Extract the binary encrypted data, key, and initialization vector
        binary_encrypted_data = file_content[:-KEY_SIZE - IVECTOR_SIZE]
        key = file_content[-(KEY_SIZE + IVECTOR_SIZE):-IVECTOR_SIZE]
        initialization_vector = file_content[-IVECTOR_SIZE:]

    return binary_encrypted_data, key, initialization_vector
