''' Program 5
 Write a Python program to generate a random number'''

# PROGRAM TO GENERATE A RANDOM NUMBER

from random import *
a='y'
while a=="y":
    a=int(input("\nEnter the starting range : "))
    b=int(input("Enter the ending range : "))
    print("\nRandom number is : ",randint(a,b))
    a=input("\nDo you want to generate again, press y : ")