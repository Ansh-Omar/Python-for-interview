''' Program 9
 Write a Python program to solve quadratic equation'''

# Solve quadratic equation

a=int(input("Enter 1st coefficient : "))
b=int(input("Enter 2nd coefficient : "))
c=int(input("Enter constant : "))
x1=((-b)+((b**2)-(4*a*c))**(1/2))/(2*a)
x2=((-b)-((b**2)-(4*a*c))**(1/2))/(2*a)
print("\nThe 2 values for x are ",x1,"and",x2)