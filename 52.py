''' Program 52
 Write a Python program to find largest number in a list'''

# LARGEST ELEMENT IN LIST

a=1;c=[]
while a == 1 :
    b=int(input("\nEnter numeric value : "))
    c.append(b)
    a=int(input("\nIf you want to insert next value,press 1,otherwise press 0 : "))
c.sort()
print("\n",c)
print("\nLargest number in list : ",c[-1])