# Program 106
'''
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1'''

def a(b):
    if b<=1:
        return 1
    else:
        return b*a(b-1)
c=int(input("Enter number : "))        
print(a(c))