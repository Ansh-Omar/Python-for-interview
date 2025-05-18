# Program 86
'''
Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list.'''

a=[1,2,3,4,5,6,7,8,9,10] # Sorted list
b=int(input("Enter element to find its index : "))
l=0;r=len(a)-1
while l<=r:
    m=(l+r)//2
    mid=a[m]
    if b == mid :
        print(b,"is in",m,"th index.")
        break
    elif b<mid: # Element is on left side
        r-=1
    elif b>mid: #Element is on right side
        l+=1
else:
    print(b,"not found in the list.")