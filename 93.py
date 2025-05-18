# Program 93
'''
Create a function that takes an angle in radians and returns the corresponding angle
in degrees rounded to one decimal place.
Examples
radians_to_degrees(1) ➞ 57.3
radians_to_degrees(20) ➞ 1145.9
radians_to_degrees(50) ➞ 2864.8
'''

from math import *
a=int(input("Enter angle in radians : "))
print("Angle in degrees : ",(a*(180/pi)))