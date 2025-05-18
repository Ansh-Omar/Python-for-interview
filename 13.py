''' Program 13
 Write a Python Program to Check Leap Year'''
 

#LEAP YEAR CHECK

# FROM SHORT METHOD

from calendar import *
a=int(input("Enter year to check it is leap or not : "))
print()
b=(isleap(a))
if b==True:
    print(a,"is leap year.")
else:
    print(a,"is not leap year.")
    
# FROM LONG METHOD

a=int(input("\nEnter year to check it is leap or not : "));print()
if ((a%4==0 and a%100!=0) or (a%400==0)):
    print(a,"is leap year.")
else:
    print(a,"is not leap year.")