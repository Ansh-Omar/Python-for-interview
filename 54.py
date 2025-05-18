'''Program 54
 Write a Python program to find N largest elements from a list'''

# N LARGEST ELEMENT IN A LIST

a=1;c=[]
while a == 1 :
    b=int(input("\nEnter numeric value : "))
    c.append(b)
    a=int(input("\nIf you want to insert next value,press 1,otherwise press 0 : "))
c.sort()
print("\n",c)
x=int(input("Which largest element you want to find ? "))
if x>len(c):
    print("invalid choice, there are",len(c),"elements in the list.")
else:
    print(x,"largest element in a list is",c[-x])