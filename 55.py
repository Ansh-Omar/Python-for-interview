'''Program 55
 Write a Python program to print even numbers in a list.'''

# EVEN NUMBER IN A LIST

x = int(input("Enter starting range : "))
y = int(input("Enter last range : "))
l=[]
for a in range(x,y+1):
    if a % 2 == 0:
        l.append(a)
print(l)