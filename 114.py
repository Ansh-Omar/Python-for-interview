# Program 114
'''
Create a function that takes the height and radius of a cone as arguments and returns
the volume of the cone rounded to the nearest hundredth. See the resources tab for
the formula.
Examples
cone_volume(3, 2) ➞ 12.57
cone_volume(15, 6) ➞ 565.49
cone_volume(18, 0) ➞ 0'''

from math import *
def a(b,c):
    return round(((1/3)*pi*(c**2)*(b)),2)
print(a(3,2))    
print(a(15,6))
print(a(18,0))