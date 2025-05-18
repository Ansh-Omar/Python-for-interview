'''Program 71
 Write a Python program to insertion at the beginning in OrderedDict'''

# INSERTION AT THE BEGINNING IN ORDERED DICT

a={2:20,3:30,4:40,5:50,6:60};b={};print(a)
c=int(input("Enter key : "))
d=int(input("Enter value : "))
b.update([(c,d)])
b.update(a)
print(b)

# ANOTHER METHOD

print("\nAnother method")
from collections import *
e={2:20,5:50,6:60,4:40,3:30};f={};print(e)
g=int(input("Enter key : "))
h=int(input("Enter value : "))
f=OrderedDict([(g,h)])
f.update(e)
print(f)