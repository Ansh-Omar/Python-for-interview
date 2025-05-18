'''Program 56
 Write a Python program to print odd numbers in a List'''

# ODD NUMBER IN A LIST

x = int(input("Enter starting range : "))
y = int(input("Enter last range : "))
l=[]
for a in range(x,y+1):
    if a % 2 != 0:
        l.append(a)
print(l)