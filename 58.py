''' Program 58
 Write a Python program to Cloning or Copying a list.'''

# CLONING OR COPYING A LIST

w=int(input("Enter how many elements you want in array : "));a=[]
for x in range(1,w+1):
    a.append(x)
b=a # ALIASING
c=a[:]
d=list(a)
e=a.copy()
print("a : ",a)
print("b : ",b)
print("c : ",c)
print("d : ",d)
print("e : ",e)
a[0]=99
print()
print("a : ",a)
print("b : ",b) # ALIASING
print("c : ",c)
print("d : ",d)
print("e : ",e)