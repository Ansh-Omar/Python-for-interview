''' Program 15 
 Write a Python Program to Print all Prime Numbers in an Interval of 1-10'''

#Python program b/w 1 to 10

y=int(input("Enter starting range : "))
z=int(input("Enter ending range : "))
for a in range(y,z+1) :
    print()
    b=0
    count=0
    for x in range(1,a+1):
        b=a%x
        if b==0:
            count+=1
    if count == 2:
        print("{} is prime".format(a))
    else:
        print("{} is not prime".format(a))