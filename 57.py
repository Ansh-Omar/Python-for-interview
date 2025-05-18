'''Program 57
 Write a Python program to Remove empty List from List'''

# REMOVE EMPTY LIST FROM LIST

a=[[1,2,3],[],[4,5],[],[6,7],[],[8,9,10],[]]
b=len(a)
x=0
while b>0:
    if ((len(a[x]))==0):
        a.pop(x)
    else:
        x+=1
    b-=1
print(a)