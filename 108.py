# Program 108
'''
Create a function that reverses a boolean value and returns the string "boolean
expected" if another variable type is given.
Examples
reverse(True) ➞ False
reverse(False) ➞ True
reverse(0) ➞ "boolean expected"
reverse(None) ➞ "boolean expected"'''

def a(b):
    if isinstance(b,bool):
        return not b
    else:
        return "Boolean expected"
print(a(True))
print(a(False))
print(a(0))
print(a(None))
print(a(1))
print(a(2))
print(a("Ansh Omar"))

# ANOTHER METHOD
print()

def a(b):
    if b==True:
        return False
    elif b==False:
        return True
    else:
        return "Boolean expected"
print(a(True))
print(a(False))
print(a(0))
print(a(None))
print(a(1))
print(a(2))
print(a("Ansh Omar"))