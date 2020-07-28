"""
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""

import zlib
import sys

print(f"Size of data is : {sys.getsizeof(b'hello world!hello world!hello world!hello world!')}")
compressed_data = zlib.compress(b"hello world!hello world!hello world!hello world!",level=9)
print(f"Size of compressed data is {sys.getsizeof(compressed_data)}")
print(f"Decompressed data is {zlib.decompress(compressed_data)}")