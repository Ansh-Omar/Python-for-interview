''' Program 44
 Write a Python program to print all disarium numbers between 1 to 100.'''

# PRINT DISARIUM NUMBER BETWEEN 1 TO 100

'''Examples : 1,2,3,4,5,6,7,8,9,89,135,175,518,598,1306,1676,2427'''

x = int(input("Enter starting range : "))
y = int(input("Enter last range : "))
for a in range(x,y+1):
    d=a
    b=len(str(a));sum = 0
    while b>0:
        c=a%10
        a//=10
        sum = sum + (c**b)
        b-=1
    if sum == d:
        print(d,'is disarium number.\n')
    else:
        print(d,'is not disarium number.\n')