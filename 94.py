# Program 94
'''
In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2
elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a
Curzon number.
Given a non-negative integer num, implement a function that returns True if num is a
Curzon number, or False otherwise.
Examples
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11
is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21
is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29
Curzon Number:
It is defined based on a specific mathematical relationship involving powers of 2. An integer
'n' is considered a Curzon number if it satisfies the following condition:
If (2^n + 1) is divisible by (2n + 1), then 'n' is a Curzon number.
For example:
If n = 5: 2^5 + 1 = 33, and 2*5 + 1 = 11. Since 33 is divisible by 11 (33 % 11 = 0), 5 is a
Curzon number.
If n = 10: 2^10 + 1 = 1025, and 2*10 + 1 = 21. 1025 is not divisible by 21, so 10 is not a
Curzon number.
Curzon numbers are a specific subset of integers with this unique mathematical property

Examples : 1,2,5,6,9,14,18,21,26,29,30,33,41,50,53,54,65,69,74,78,81,86,89,90,98'''

a=int(input("Enter number to check whether it is curzon number or not : "))
b=(2**a)+1
c=(2*a)+1
if b%c==0:
    print(a,"is curzon number.")
else:
    print(a,"is not curzon number.")
    
z=int(input("\nEnter starting limit : "))
y=int(input("Enter last limit : "))
for a in range(z,y+1):
    b=(2**a)+1
    c=(2*a)+1
    if b%c==0:
        print("\n",a,"is curzon number.")
    else:
        print("\n",a,"is not curzon number.")