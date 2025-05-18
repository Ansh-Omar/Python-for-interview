''' Program 60
 Write a Python program to find words which are greater than given length k'''

'''FIND WORDS WHICH ARE GREATER THAN GIVEN LENGTH K'''

a=1;c=[];g=[]
while a == 1 :
    b=(input("\nEnter word : "))
    c.append(b)
    a=int(input("\nIf you want to insert next value,press 1,otherwise press 0 : "))
d=len(c)
k=int(input("\nEnter the length of word : "))
for x in range(d):
    if (len(c[x]))>k:
        f=c[x]
        g.append(f)
print("\nWords greater than",k,"letters are : ",g)