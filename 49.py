'''Program 49
Write a program to find sum of elements in list'''

# SUM OF ELEMENTS IN LIST

a=1;c=[]
while a == 1 :
    b=int(input("\nEnter numeric value : "))
    c.append(b)
    a=int(input("\nIf you want to insert next value,press 1,otherwise press 0 : "))
print()
for x in range(len(c)-1):
    print(c[x],end=" + ")
print(c[-1]," = ",end="")
print(sum(c))