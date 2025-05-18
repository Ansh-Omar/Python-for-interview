'''Program 41
 Write a Python Program to Remove Punctuation From a String'''

# REMOVE PUNCTUATION FROM STRING

pun = '''`~!@#$%^&*()-_=+[{}]\|;:'",<.>/?'''
a = input("Enter string  : ")
for x in a:
    if x not in pun:
        print(x,end="")
    else:
        continue