'''Program 73
 Write a Python program to sort Python Dictionaries by Key or Value'''

# SORT DICTIONARY BY KEY

a={4:10,5:20,1:50,3:40,6:60,2:30};b={}
for x in sorted(a):
    b.update([(x,a[x])])
print(b)

# SORT DICTIONARY BY VALUE

a={4:10,5:20,1:50,3:40,6:60,2:30};b={}
for x in sorted(a,key=a.get):
    b.update([(x,a[x])])
print(b)