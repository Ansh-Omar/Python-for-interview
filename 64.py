'''Program 64
 Write a Python program to find uncommon words from two Strings.'''

# FIND UNCOMMON WORDS FROM TWO STRING

a = input("Enter first string : ")
b = input("Enter second string : ")
f=[];g=[];h=[]
c,d=a.split(),b.split()
if len(c)>len(d):
    e=len(c)
    f=c[:]
    g=d[:]
else:
    e=len(d)
    f=d[:]
    g=c[:]
for x in range(e):
    if f[x] not in g:
        h.append(f[x])
    if g[x] not in f:
        h.append(g[x])
print("Uncommon words are : ",set(h))