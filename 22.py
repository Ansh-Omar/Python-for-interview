''' Program 22
 Write a Python Program to Find LCM.
 Least Common Multiple (LCM):
 LCM, or Least Common Multiple, is the smallest multiple that is exactly divisible by two or
 more numbers.
 Formula:
 For two numbers a and b, the LCM can be found using the formula:
 LCM(𝑎,𝑏) =  |𝑎⋅𝑏| upon GCD(𝑎,𝑏)
 For more than two numbers, you can find the LCM step by step, taking the LCM of pairs of
 numbers at a time until you reach the last pair.
 Note: GCD stands for Greatest Common Divisor.'''

# PROGRAM TO FIND LCM

a=int(input("Enter number : "));j=a
b=int(input("Enter number : "));k=b
if a>b:
    c=a
else:
    c=b
while (True):
    if ((c%a==0) and (c%b==0)):
        lcm=c
        break
    c+=1
print("LCM of",j,"and",k,"is",lcm)