''' Program 14
 Write a Python Program to Check Prime Number.
 Prime Numbers:
 A prime number is a whole number that cannot be evenly divided by any other number
 except for 1 and itself. For example, 2, 3, 5, 7, 11, and 13 are prime numbers because they
 cannot be divided by any other positive integer except for 1 and their own value'''

# PRIME NUMBER 

a=int(input("Enter number : "))
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