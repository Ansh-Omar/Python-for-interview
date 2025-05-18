'''Program 63
 Write a Python program to check if a given string is binary string or not.'''

# BINARY STRING

a=input("Enter string : ");count=0
for x in range(len(a)):
    if a[x]=='0' or a[x]=='1' :
        count=count+1
if count==len(a):
    print(a,"is binary string.")
else:
    print(a,"is not binary string.")