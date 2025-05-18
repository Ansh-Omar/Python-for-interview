# Program 139
'''
Write a function that creates a dictionary with each (key, value) pair being the (lower
case, upper case) versions of a letter, respectively.
Examples
mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
Notes
All of the letters in the input list will always be lowercase'''

def a(b):
    c={}
    for x in b:
        c.update([(x,x.upper())])
    print(c)
a(["p","s"])            
a(["a", "b", "c"])
a(["a", "v", "y", "z"])