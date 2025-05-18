# Program 129
'''
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414
Notes
The function receives an integer and must return an integer'''

def a(b):
    for x in str(b):
        print((int(x)**2),end="")
    print()        
a(9119)
a(2483)        
a(3212)