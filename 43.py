''' Program 43
 Write a Python program to check if the given number is a Disarium Number.
 1
 2
 A Disarium number is a number that is equal to the sum of its digits each raised to the
 power of its respective position. For example, 89 is a Disarium number because
 8 to the power 1 + 9 to the power 2 = 8 + 81 = 89 '''

# DISARIUM NUMBER

''' 89 is a disarium nnumber.
8 to the power 1 + 9 to the power 2 = 89
# Examples : 1,2,3,4,5,6,7,8,9,89,135,175,518,598,1306,1676,2427'''

a = int(input("Enter number : "));d=a
b=len(str(a));sum = 0
while b>0:
    c=a%10
    a//=10
    sum = sum + (c**b)
    b-=1
if sum == d:
    print(d,'is disarium number.')
else:
    print(d,'is not disarium number.')