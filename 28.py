'''Program 28
 Write a Python Program to Find Factorial of Number Using Recursion.
 The factorial of a non-negative integer ( n ) is the product of all positive integers less than or
 equal to ( n ). It is denoted by ( n! ) and is defined as:
 𝑛! = 𝑛×(𝑛−1)×(𝑛−2)×…×3×2×1
 For example:
 is defined to be 1.
 5! = 5×4×3×2×1=120
 0!
 Factorials are commonly used in mathematics, especially in combinatorics and probability,
 to count the number of ways a set of elements can be arranged or selected.'''

# FACTORIAL OF NUMBER USING RECURSION

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        f=n*fact(n-1)
        return f
a=int(input("Enter number : "))
print("Factorial of",a,"is",fact(a))