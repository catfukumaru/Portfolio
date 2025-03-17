import unittest
from compression import *
import lzma

class TestCompressionLZMA(unittest.TestCase):
    """tests a variety of byte strings with the compression_lzma function"""
    # @unittest.skip("")
    def test_compress_small_pdf(self):
        small_pdf = b"%PDF-1.4\n1 0 obj\n<< /Title (Small PDF) >>\nendobj\n%%EOF"
        compressed = compression_lzma(small_pdf)
        self.assertIsInstance(compressed, bytes) # checks the type
        self.assertNotEqual(compressed, small_pdf)  # Checks if the sample string is compressed

    # @unittest.skip("")
    def test_compress_medium_pdf(self):
        medium_pdf = b"%PDF-1.4\n" + b"1 0 obj\n<< /Title (Medium PDF) >>\nendobj\n" * 100 + b"%%EOF"
        compressed = compression_lzma(medium_pdf)
        self.assertIsInstance(compressed, bytes)    # checks the type
        self.assertNotEqual(compressed, medium_pdf)   # Checks if the sample string is compressed

    # @unittest.skip("")
    def test_compress_large_pdf(self):
        large_pdf = b"%PDF-1.4\n" + b"1 0 obj\n<< /Title (Large PDF) >>\nendobj\n" * 1000 + b"%%EOF"
        compressed = compression_lzma(large_pdf)
        self.assertIsInstance(compressed, bytes)    # checks the type
        self.assertNotEqual(compressed, large_pdf)   # Checks if the sample string is compressed

    # @unittest.skip("")
    def test_compress_empty_pdf(self):
        empty_pdf = b""
        compressed = compression_lzma(empty_pdf)
        self.assertIsInstance(compressed, bytes) # checks the type
        self.assertNotEqual(compressed, empty_pdf)   # Checks if the sample string is compressed

class TestDecompressionLZMA(unittest.TestCase):
    """tests a variety of compressed byte strings"""
    def setUp(self):
        # Sample PDF data of varying sizes
        self.small_pdf = b"%PDF-1.4\n1 0 obj\n<< /Title (Small PDF) >>\nendobj\n%%EOF"
        self.medium_pdf = b"%PDF-1.4\n" + b"1 0 obj\n<< /Title (Medium PDF) >>\nendobj\n" * 100
        self.large_pdf = b"%PDF-1.4\n" + b"1 0 obj\n<< /Title (Large PDF) >>\nendobj\n" * 1000

        # Compress the data
        self.compressed_small_pdf = lzma.compress(self.small_pdf, check=lzma.CHECK_SHA256)
        self.compressed_medium_pdf = lzma.compress(self.medium_pdf, check=lzma.CHECK_SHA256)
        self.compressed_large_pdf = lzma.compress(self.large_pdf, check=lzma.CHECK_SHA256)

    @unittest.skip("")
    def test_decompress_small_pdf(self):
        decompressed = decompression_lzma(self.compressed_small_pdf)
        self.assertEqual(decompressed, self.small_pdf)

    @unittest.skip("")
    def test_decompress_medium_pdf(self):
        decompressed = decompression_lzma(self.compressed_medium_pdf)
        self.assertEqual(decompressed, self.medium_pdf)

    @unittest.skip("")
    def test_decompress_large_pdf(self):
        decompressed = decompression_lzma(self.compressed_large_pdf)
        self.assertEqual(decompressed, self.large_pdf)

    @unittest.skip("")
    def test_decompress_empty_pdf(self):
        empty_pdf = b""
        compressed_empty_pdf = lzma.compress(empty_pdf, check=lzma.CHECK_SHA256)
        decompressed = decompression_lzma(compressed_empty_pdf)
        self.assertEqual(decompressed, empty_pdf)


if __name__ == '__main__':
    unittest.main()


# used:
#   https://medium.com/@jberkenbilt/the-structure-of-a-pdf-file-6f08114a58f6
#   https://opensource.adobe.com/dc-acrobat-sdk-docs/standards/pdfstandards/pdf/PDF32000_2008.pdf