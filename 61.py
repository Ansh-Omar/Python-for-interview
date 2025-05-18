''' Program 61
 Write a Python program for removing 
�
�ℎ
 𝑖
 character from a string'''

# REMOVE Nth CHARACTER FROM A STRING

a = input("Enter string : ")
b=int(input("Which no. of character you want to remove ? "))
print("After removing",a,"th character from string",a[:b-1],end="")
print(a[(b):])