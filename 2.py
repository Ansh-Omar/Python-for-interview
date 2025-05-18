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