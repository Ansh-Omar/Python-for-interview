'''Program 10
 Write a Python program to swap two variables without temp variable'''

# Swap two variable without 3rd variable

#for numeric  values

a=int(input("Enter numerical value  : "))
b=int(input("Enter  numerical value : "))
print("\nBefore swapping : \na : ",a,"\nb : ",b)
a=a+b
b=a-b
a=a-b
print("\nAfter swapping : \na : ",a,"\nb : ",b)

# for string

a=input("\nEnter string : ")
b=input("Enter string : ")
print("\nBefore swapping : \na : ",a,"\nb : ",b)
a,b=b,a
print("\nAfter swapping : \na : ",a,"\nb : ",b)