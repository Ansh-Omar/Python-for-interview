'''Program 53
 Write a Python program to find second largest number in a list'''

# SECOND LARGEST ELEMENT IN A LIST

a=1;c=[]
while a == 1 :
    b=int(input("\nEnter numeric value : "))
    c.append(b)
    a=int(input("\nIf you want to insert next value,press 1,otherwise press 0 : "))
c.sort()
print("\n",c)
if len(c)==1:
    print("\nSecond largest number in list : ",c[0])
else:
    print("\nSecond largest number in list : ",c[-2])