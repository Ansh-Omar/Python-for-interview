# Program 122
'''
Create a function that takes three parameters where:
- x is the start of the range (inclusive).
- y is the end of the range (inclusive).
- n is the divisor to be checked against.
Return an ordered list with numbers in the range that are divisible by the third
parameter n.
Return an empty list if there are no numbers that are divisible by n.

Examples

list_operation(1, 10, 3) ➞ [3, 6, 9]

list_operation(7, 9, 2) ➞ [8]

list_operation(15, 20, 7) ➞ []'''

def a(b,c,d):
    e=[]
    for x in range(b,c+1):
        if x%d==0:
            e.append(x)
    print(e)            
a(1,10,3)    
a(7,9,2)
a(15,20,7)