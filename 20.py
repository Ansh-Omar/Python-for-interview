'''Program 20
 Write a Python Program to Find Armstrong Number in an Interval'''

# CHECK ARMSTRONG NUMBER IN RANGE

p=int(input("Enter start range : "))
t=int(input("Enter last range : "))
for w in range(p,t+1):
    b=(len(str(w)));q=w;e=0;r=b
    for x in range(1,r+1):
        c=w%10
        e=e+c**b
        w=w//10
    if q==e:
        print(q,"is armstrong number.")
    else:
        print(q,"is not armstrong number.")