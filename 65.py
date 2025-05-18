'''Program 65
 Write a Python program to find all duplicate characters in string'''

# FIND ALL DUPLICATE CHARACTERS IN STRING

a = input("Enter string : ");b=[]
c=a.lower()
print(c)
for x in range(len(c)):
    if c[x] in c[(x+1):]:
        if c[x]!=" ":
            b.append(c[x])
print(set(b))