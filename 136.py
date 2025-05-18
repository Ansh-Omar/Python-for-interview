# Program 136
'''
Create a function that validates whether three given integers form a Pythagorean
triplet. The sum of the squares of the two smallest integers must equal the square of
the largest number to be validated.
Examples
is_triplet(3, 4, 5) ➞ True
3² + 4² = 25
5² = 25
is_triplet(13, 5, 12) ➞ True
5² + 12² = 169
13² = 169
is_triplet(1, 2, 3) ➞ False
1² + 2² = 5
3² = 9
Notes
Numbers may not be given in a sorted order.'''

def a(b,c,d):
    e=[b,c,d]
    e.sort()
    if (( (e[0])**2 + (e[1])**2 ) == (e[2])**2 ):
        print(True)
    else:
        print(False)        
a(3,4,5)        
a(13,5,12)
a(1,2,3)