from itertools import compress

import os
import file_handler
import compression
import encryption

"""
main file for the encryptor
"""

# get the input
print("This is a PDF encryptor. This only works on Windows. Do not change the name of \"encrypted.bin\" that is where the encrypted file is stored ")
en_or_de = input("Do you want to encrypt(E) or decrypt(D): \n")
if en_or_de.upper() == 'E':
    print("please input the full directory path and filename")

    directory_path = input("full directory path: ")
    directory_path= r'{}'.format(directory_path) # to escape the backslashes

    filename = input("filename: ")

    full_path = ""

    # if the format of the directory path and the filename are correct then get the file's full path
    if file_handler.directory_path_format(directory_path) and file_handler.filename_format(filename):
        full_path = file_handler.locate_folder(directory_path, filename)
        #full_path = full_path[0] # test this later

    if file_handler.determine_PDF_bytes(full_path): # if the file is a PDF

        with open(full_path, 'rb') as pdf_in_binary:
            pdf_contents = pdf_in_binary.read()     # gets the contents of the pdf

        compressed_pdf_contents = compression.compression_lzma(pdf_contents)    # compresss the dile
        encrypted_pdf_contents, key, initialization_vector = encryption.encryption_Blowfish(compressed_pdf_contents) # encrypts the file

        fullfilepath = os.path.join(directory_path, 'encrypted.bin') # filepath for where the encrypted contents of the pdf are going. i.e it will be in the same folder as the original pdf

        file_handler.write_into_file(fullfilepath, encrypted_pdf_contents, key, initialization_vector) # writes the transformed contents into a bin file
        print("Your file has been encrypted.")

elif en_or_de.upper() == 'D':
    print("please input the full directory path and the new name you want the decrypted file to have")

    directory_path = input("full directory path: ")
    directory_path = r'{}'.format(directory_path)  # to escape the backslashes

    filename = input("filename: ")

    full_path = ""

    if file_handler.directory_path_format(directory_path): #
        full_path = file_handler.locate_folder(directory_path, "encrypted.bin") # get the full path to the file encrypted file

    with open(full_path, 'rb') as encrypted_file: # decrypt the file
        encrypted_file_contents = encrypted_file.read()

        data_and_attributes = file_handler.get_values(full_path)
        compressed_file_contents = encryption.decryption_Blowfish(data_and_attributes)
        file_contents = compression.decompression_lzma(compressed_file_contents)

    if file_handler.filename_format(filename): # if the file name is in the correct format then make a new path with it
        fullfilepath = os.path.join(directory_path, filename)
        with open(fullfilepath, 'wb') as file: # open the new file and put the contents in it
            file.write(file_contents)
        print(f"the file has been decrypted and stored in {filename}")
    else:
        print("new filename is not correct. maybe you forgot to add the extension to it?")

else:
    print("wrong input run the program again")