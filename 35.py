'''Program 35
 Write a Python Program to Split the array and add the first part to the end'''

# SPLIT THE ARRAY AND ADD FIRST PART TO THE END

w=int(input("Enter how many elements you want in array : "));a=[]
for x in range(1,w+1):
    a.append(x)
print("\n",a);l=a[:]
for x in range(10):
    b=int(input("\nEnter how many elements you want to split : "))
    if b<=len(a):
        for x in range(len(a)):
            l[-b]=a[x]
            b-=1
        print(l)
    else :
        while(b>len(a)):
            b-=len(a)
        for x in range(len(a)):
            l[-b]=a[x]
            b-=1
        print(l)