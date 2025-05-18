''' Program 36
 Write a Python Program to check if given array is Monotonic.
 A monotonic array is one that is entirely non-increasing or non-decreasing.'''

# TO CHECK IF GIVEN ARRAY IS MONOTONIC

a=1;c=[]
while a == 1 :
    b=int(input("\nEnter numeric value : "))
    c.append(b)
    a=int(input("\nIf you want to insert next value,press 1,otherwise press 0 : "))
print("\n",c);d=len(c);e=0;f=1;g=d
count=1
while (d>0) and (f<g) :
    if c[e]>=c[f] or c[e]<=c[f] :
        count+=1
        e,f=f,f+1
    d-=1
if count ==g:
    print("\nArray is monotonic")
else:
    print("\nArray is not monotonic") 