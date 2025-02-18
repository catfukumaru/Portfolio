''' deals with handling the file
todo: make this module description more detailed'''
import os
import re

def locate_folder(directory, filename):
    """
        find the folder in a drive of the computer the program is running on

        param: location = string
        returns: operating_system.folder_object(location) = folder_object # object that handles operations to do with a folder in a computer system
    """
# no need to grant access


    for root, dirs, files in os.walk(directory):
        for file in files:
             if file == filename:
                return (os.path.join(root,file))
             else:
                print("the path was not found, try again")
    return None





# the user needs to add the extra backslash


# --- new function, checks the format of the directory path
def directory_path_format(directory_string):
    pattern = r'^[a-zA-Z]:\\(((?![<>:"/\\|?*]).)+((?<![ .])\\)?)*$'  # pattern for the patth of the folder

    # Regex Pattern explanation:
    #     ^ [A - Z]: ensures that the path starts with a drive letter (A-Z) followed by a colon.
    #
    #     \\ matches a backslash.
    #
    #     (?:[\w\s\-\.]+\\) * matches zero or more directory names followed by a backslash. Each directory name can
    #     contain word characters(\w), spaces(\s), hyphens(-), and periods(.).
    #
    #     [\w\s\-\.]+$ ensures that the path ends with a directory name (without a trailing backslash).

    if re.match(pattern, directory_string):  # check is the format of the location is correct
        return True
    else:
        # Identify the part of the path that is wrong
        if not re.match(r'^[a-zA-Z]:\\ ', directory_string):
            print("Error: The path must start with a drive letter followed by a colon and backslash (e.g., C:\\).")
        elif not re.search(r'\\+', directory_string): # ? if this is relevant cause the top one already those this check
            print("Error: The path must contain at least one backslash (\\) to separate directories.")
        else:
            # Check for invalid characters in the path
            invalid_chars = re.findall(r'[<>:"/\\|?*]', directory_string)
            if invalid_chars:
                print(f"Error: The path contains invalid characters: {', '.join(set(invalid_chars))}.")
                print("Please remove these characters from the path.")

    return False

def filename_format(file_string):# i was here make test cases fro this
    
    pattern = r'^[^\t\r\n\\\/<>:"|?*]*[^\t\r\n\\\/<>:"|?*.\s]\.(pdf|PDF)$'
    if re.match(pattern, file_string):  # check is the format of the location is correct
        return True
    else:
        print("this program only accepts PDF files")
        return False



def determine_PDF_bytes(filename_with_extension):
    """determine whether a file is a pdf by the first few bytes in the file"""

    with open(filename_with_extension, "rb") as file:
        first_four_bytes= file.read(4)

    if first_four_bytes == b'%PDF':
        return True
    else:
        print("The file you have choosen is of the wrong format. Please only use PDF files")
        return False

def pdf_to_bytes(filename_with_extension):
    """determine whether a file is a pdf by the first few bytes in the file"""
    full_file = b''
    with open(filename_with_extension, "rb") as file:
        while True:
            part_of_file = file.read(1024)
            if not part_of_file:
                break
            full_file+=part_of_file

    return full_file







    # print ("the path was written incorrectly, try again")
# my_commandline.ask_folder_path()  # asks the user for the folder path again from another file that handles the obtaining values from the command line
# ----
#
#
# ---onece i get the main functionaly working i can add this to it
# IF
# operating_system.search(location) == type(path_object):  # if the search produces an path_object
# return operating_system.folder_object(location)
# ELSE:
# # print ("the path was not found, try again")
# my_commandline.ask_folder_path()  # asks the user for the folder path again