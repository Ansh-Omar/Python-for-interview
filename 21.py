'''Program 21
 Write a Python Program to Find the Sum of Natural Numbers.
 Natural numbers are a set of positive integers that are used to count and order objects.
 They are the numbers that typically start from 1 and continue indefinitely, including all the
 whole numbers greater than 0. In mathematical notation, the set of natural numbers is often
 denoted as "N" and can be expressed as:
 𝑁 =1,2,3,4,5,6,7,8,...'''

# SUM OF NATURAL NUMBER

p=int(input("Enter start range : "))
t=int(input("Enter last range : "))
n=(t+1)-p
print("The sum of natural number from",p,"to",t,"is",((n/2)*((2*p)+(n-1))))