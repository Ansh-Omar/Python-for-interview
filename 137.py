# Program 137
'''
Create a function that takes three integer arguments (a, b, c) and returns the amount
of integers which are of equal value.
Examples
equal(3, 4, 3) ➞ 2
equal(1, 1, 1) ➞ 3
equal(3, 4, 1) ➞ 0
Notes
Your function must return 0, 2 or 3'''

def a(b,c,d):
    e=[b,c,d];f=set(e)
    if len(f)==len(e):
        print(0)
    elif len(f)==2:
        print(2)
    elif len(f)==1:
        print(3)        
a(3,4,3)        
a(1,1,1)
a(3,4,1)