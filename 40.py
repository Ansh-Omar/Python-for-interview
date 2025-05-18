'''Program 40
 Write a Python Program to Sort Words in Alphabetic Order.'''

# SORT WORDS IN ALPHABETIC ORDER

u='y';a=[]
while u == 'y':
    w=input("Enter string : ")
    a.append(w)
    u=input(" If you want to continue, press y otherwise n : ")
c={}
for x in range(len(a)):
    b=a[x].title()
    d=(ord(b[0]))
    c[d]=b
print()
for y in sorted(c.keys()):
    print(c[y])
    
# ANOTHER WAY

a=input("\nEnter words with space: ")
b=[c.capitalize() for c in a.split()]
b.sort()
for x in range(len(b)):
    print(b[x])
    
# ANOTHER WAY

u='y';a=[];d=[]
while u == 'y':
    w=input("\nEnter string : ")
    a.append(w)
    u=input(" If you want to continue, press y otherwise n : ")
for x in range(len(a)):
    b=a[x].title()
    d.append(b)
d.sort()
for c in d:
    print(c)