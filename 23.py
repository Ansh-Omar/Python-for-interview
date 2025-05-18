''' Program 23
 Write a Python Program to Find HCF.
 Highest Common Factor(HCF):
 HCF, or Highest Common Factor, is the largest positive integer that divides two or more
 numbers without leaving a remainder.
 Formula:
 For two numbers a and b, the HCF can be found using the formula:
 HCF(𝑎,𝑏) = GCD(𝑎,𝑏)
 For more than two numbers, you can find the HCF by taking the GCD of pairs of numbers at
 a time until you reach the last pair.
 Note: GCD stands for Greatest Common Divisor'''


# PROGRAM TO FIND HCF

'''a=int(input("Enter number : "));j=a
b=int(input("Enter number : "));k=b
if a>b:
    c=a
else:
    c=b
while(True):
    if((c%a==0)and(c%b==0)):
        l=c
        break
    c+=1
print("HCF of",j,"and",k,"is",int((a*b)/l))'''

# ANOTHER WAY

#CALCULATING HCF

'''a=int(input('Enter the number '))
b=int(input('Enter the number '))

def HCF(a,b):
	if a==0:
		return b
	return HCF(b%a,a)
ans=HCF(a,b)
print(f'HCF of {a} and {b} :',ans)'''