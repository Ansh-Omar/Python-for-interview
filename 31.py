'''Program 31
 Write a Python Program for cube sum of first n natural numbers?'''

# CUBE SUM OF FIRST N NATURAL NUMBER

a=int(input("Enter limit : "));sum=0;b=a
while a>0:
    sum+=(a**3)
    a-=1
print("1^3",end="")
for x in range(2,b+1):
    print(" + ",x,"^3",sep="",end="")
print(" = ",sum)