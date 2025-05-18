''' Program 19
 Write a Python Program to Check Armstrong Number?
 Armstrong Number:
 It is a number that is equal to the sum of its own digits, each raised to a power equal to the
 number of digits in the number.
 For example, let's consider the number 153:
 It has three digits (1, 5, and 3).
 If we calculate 1 cube + 5 cube + 3 cube, we get 1+125+27, which is equal to 153.
 So, 153 is an Armstrong number because it equals the sum of its digits raised to the power
 of the number of digits in the number.'''

#ARMSTRONG NUMBER

a=int(input("Enter number : "))
b=(len(str(a)));q=a;e=0;r=b
for x in range(1,r+1):
    c=a%10
    e=e+c**b
    a=a//10
if q==e:
    print(q,"is armstrong number.")
else:
    print(q,"is not armstrong number.")