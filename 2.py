 '''Program 2
 Write a Python program to do arithmetical operations addition and division'''

# ARITHMETIC OPERATION

a=int(input("Enter no. : "))
b=int(input("Enter no. : "))
c=input("Enter 1 operator (+ , - , * , / , // , ** , %) : ")
if c=="+":
    print("a+b = ",a+b)
if c=="-":
    print("a-b = ",a-b)
if c=="*":
    print("a*b = ",a*b)
if c=="/":
    if b==0:
        print("Division by zero is infinity")
    else:
        print("a/b = ",a/b)
if c=="//":
    if b==0:
        print("Division by zero is infinity")
    else:
        print("a//b = ",a//b)    
if c=="**":
    print("a**b = ",a**b)
if c=="%":
    print("a%b = ",a%b)    
