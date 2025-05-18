# Program 125
'''
An isogram is a word that has no duplicate letters. Create a function that takes a
string and returns either True or False depending on whether or not it's an "isogram".
Examples
is_isogram("Algorism") ➞ True
is_isogram("PasSword") ➞ False
- Not case sensitive.
is_isogram("Consecutive") ➞ False
Notes
Ignore letter case (should not be case sensitive).
All test cases contain valid one word strings'''

def a(b):
    c=b.lower()
    if len(list(c))==len(set(c)):
        print(True)
    else:
        print(False)        
a("Algorism")        
a("PasSword")
a("Consecutive")