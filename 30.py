''' Program 30
 Write a Python Program to calculate the natural logarithm of any number.'''

# NATURAL LOGARITHM OF ANY NUMBER

from math import *
def a():
    b=float(input("\nEnter positive number : "))
    if b<=0:
        print("\nPlease enter a positive number.")
        a()
    else:
        print("\nNatural logarithm of",b,"is",log(b))
        #a()
a()