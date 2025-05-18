# Program 133
'''
Create a function that takes a list of numbers and return the number that's unique.
Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7
unique([0, 0, 0.77, 0, 0]) ➞ 0.77
unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0
Notes
Test cases will always have exactly one unique number while all others are the same'''

def a(b):
    b.sort()
    if b[0]==b[1]:
        print(b[-1])
    else:
        print(b[0])        
a([3, 3, 3, 7, 3, 3])
a([0, 0, 0.77, 0, 0])
a([0, 1, 1, 1, 1, 1, 1, 1])        