# Program 85
'''
Please write a program to compress and decompress the string "hello world!hello
world!hello world!hello world!".'''

from zlib import *
a = "hello world!hello world!hello world!hello world!"
b = compress(a.encode())
print(f"Compressed string : {b}")
c = decompress(b).decode()
print(f"Decompressed string : {c}")