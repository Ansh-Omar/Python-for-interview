# Program 111
'''
Using list comprehensions, create a function that finds all even numbers from 1 to
the given number.
Examples
find_even_nums(8) ➞ [2, 4, 6, 8]
find_even_nums(4) ➞ [2, 4]
find_even_nums(2) ➞ [2]'''

def a(b):
    c=[x for x in range(1,b+1) if x%2==0]
    print(c)
a(8)    
a(4)
a(2)