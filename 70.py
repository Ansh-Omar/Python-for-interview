''' Program 70
 Write a Python program to convert key-values list to flat dictionary'''

# CONVERT KEY VALUE LIST TO FLAT DICTIONARY

a=[(1,"Apple"),(2,"Banana"),(3,"Cat"),(4,"Dog")]
b=dict(a)
print(b)
for x in b:
    print(x," : ",b[x])