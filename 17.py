'''Program 17
 Write a Python Program to Display the multiplication Table'''

#TABLE

a=int(input("Enter no. : "))
b=int(input("Enter limit : "))
print()
for x in range(1,b+1):
    print(a,"X",x,"=",a*x)