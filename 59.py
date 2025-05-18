'''Program 59
 Write a Python program to Count occurrences of an element in a list'''

# COUNT OCCURRENCES OF ELEMENTS IN LIST

a=[1,2,3,4,1,5,1,6,1,7,8,1]
print(a);b=0
x=int(input("Enter of which element occurrences you want to see : "))
if x not in a:
    print("Invalid choice,",x,"is not present in the list.")
else:
    b=a.count(1)
print(x,"occur",b,"times.")