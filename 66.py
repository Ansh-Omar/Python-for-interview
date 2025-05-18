''' Program 66
 Write a Python Program to check if a string contains any special character'''

# TO CHECK IF STRING CONTAINS ANY SPECIAL CHARACTER OR NOT

a = input("Enter string : ");count=0
b='''`~!@#$%^&*()-_=+[]{}\|;''"":,./<>?'''
for x in a:
    if x in b:
        count+=1
if count>0:
    print("String contains special character.")
else:
    print("String not contains any special charcater.")