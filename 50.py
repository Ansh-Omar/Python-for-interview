'''Program 50
 Write a Python program to Multiply all numbers in the list.'''

# MULTIPLY ALL ELEMENTS IN LIST

a=1;c=[];pro=1
while a == 1 :
    b=int(input("\nEnter numeric value : "))
    c.append(b)
    a=int(input("\nIf you want to insert next value,press 1,otherwise press 0 : "))
print()
for x in range(len(c)-1):
    print(c[x],end=" * ")
print(c[-1]," = ",end="")
for x in range(len(c)):
    pro*=c[x]
print(pro)