''' Program 34
 Write a Python Program for array rotation.'''

# PYTHON PROGRAM FOR ARRAY ROTATION

w=int(input("Enter how many elements you want in array : "));a=[]
for x in range(1,w+1):
    a.append(x)
print("\n",a);l=a[:]
for x in range(10):
    b=int(input("\nEnter, to how many positions you want to rotate : "))
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