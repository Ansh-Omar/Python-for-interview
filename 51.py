''' Program 51
 Write a Python program to find smallest number in a list'''

# SMALLEST NUMBER IN LIST

a=1;c=[]
while a == 1 :
    b=int(input("\nEnter numeric value : "))
    c.append(b)
    a=int(input("\nIf you want to insert next value,press 1,otherwise press 0 : "))
c.sort()
print("\n",c)
print("\nSmallest number in list : ",c[0])