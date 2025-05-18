# Program 128
'''
Given a string of numbers separated by a comma and space, return the product of
the numbers.
Examples
multiply_nums("2, 3") ➞ 6
multiply_nums("1, 2, 3, 4") ➞ 24
multiply_nums("54, 75, 453, 0") ➞ 0
multiply_nums("10, -2") ➞ -20'''

def a(b):
    p=1
    for x in b.split(","):
        p*=int(x)
    print(p)            
a("2,3")    
a("1,2,3,4")
a("54, 75, 453, 0")
a("10, -2")