import lzma

"""
This file compresses and decompresses a byte string using the LZMA algorithm
"""


def compression_lzma(pdf_file):
    """
    compresses a file

    param: pdf_file = bytes string
    returns: compressed_file = byte string
    """

    compressed_file = lzma.compress(pdf_file, check=lzma.CHECK_SHA256)      # data is compressed and it includes an integrity checker

    return compressed_file


def decompression_lzma(pdf_file):
    """
    decompresses a file

    param:
        pdf_file = bytes string
    returns:
        decompressed_file = bytes string
    """

    lzc = lzma.LZMADecompressor()
    decompressed_file = lzc.decompress(pdf_file)
    if lzc.check == lzma.CHECK_SHA256:
        print("Data integrity check was successfully.")
    else:
        print("Data integrity check was not successfully: data could be corrupted.")

    return decompressed_file


# used https://docs.python.org/3.13/library/lzma.html