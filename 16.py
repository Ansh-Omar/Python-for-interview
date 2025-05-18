''' Program 16
 Write a Python Program to Find the Factorial of a Number'''

# Factorial

a=int(input("Enter number : "))
b=1;c=a
while a>0:
    b=a*b
    a-=1
print("\nFactorial of",c,"is",b)