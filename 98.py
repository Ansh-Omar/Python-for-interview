# Program 98
'''
Create a function that returns True if a given inequality expression is correct and
False otherwise.
Examples
correct_signs("3 < 7 < 11") ➞ True
correct_signs("13 > 44 > 33 <1") ➞ False
correct_signs("1 < 2 < 6 < 9 > 3") ➞ True'''

# First method
def a(b):
    print(eval(b))
a("1 < 2 < 6 < 9 > 3")
a("3 < 7 < 11")
a("13 > 44 > 33 <1")

print()

# Second method
def a(b):
    print(b)
a(1 < 2 < 6 < 9 > 3)
a(3 < 7 < 11)
a(13 > 44 > 33 <1)