''' Program 26
 Write a Python Program to Make a Simple Calculator with 4 basic mathematical
 operations.'''

# CALCULATOR

c='y'
while c=="y" or "Y":
    a=float(input("Enter number : "))
    b=float(input("Enter number : "))
    print("\n1 : ADDITION\n2 : SUBTRACTION\n3 : MULTIPLICATION\n4 : DIVISION")
    d=int(input("\nEnter your choice : "))
    if d==1:
        print("\n",a+b)
        c=(input("\nIf you want to perform another operation, press y."))
    elif d==2:
        print("\n",a-b)
        c=(input("\nIf you want to perform another operation, press y."))
    elif d==3:
        print("\n",a*b)
        c=(input("\nIf you want to perform another operation, press y."))
    elif d==4:
        print("\n",a/b)
        c=(input("\nIf you want to perform another operation, press y."))
    else:
        print("Invalid choice.")
        c=(input("\nIf you want to perform another operation, press y."))