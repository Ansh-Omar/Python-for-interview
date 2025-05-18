'''Program 72
 Write a Python program to check order of character in string using OrderedDict()'''

# CHECK ORDER OF CHARACTER IN STRING USING ORDERED DICT()

from collections import *
a=input("Enter string : ")
b=input("Enter string : ")
c=OrderedDict.fromkeys(a)
d=OrderedDict.fromkeys(b)
print(c)
print(d)
if (c == d) :
    print("The order of characters in the first string matches the second string.")
else:
    print("The order of characters in the first string does not matches the second string.")
    
# OUTPUT
'''
Enter string : Ashish Kumar Shukla
Enter string : Ashi Kumar Skl
OrderedDict([('A', None), ('s', None), ('h', None), ('i', None), (' ', None), ('K', None), ('u', None), ('m', None), ('a', None), ('r', None), ('S', None), ('k', None), ('l', None)])
OrderedDict([('A', None), ('s', None), ('h', None), ('i', None), (' ', None), ('K', None), ('u', None), ('m', None), ('a', None), ('r', None), ('S', None), ('k', None), ('l', None)])
The order of characters in the first string matches the second string.

[Program finished]
'''