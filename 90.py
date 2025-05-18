# Program 90
'''
Assuming that we have some email addresses in the
"username@companyname.com (mailto:username@companyname.com)" format,
please write program to print the user name of a given email address. Both user
names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com (mailto:john@google.com)
Then, the output of the program should be:
john'''

a=input("Enter email address without using any digit in this format --> username@companyname.com : ")
for x in range(len(a)):
    print(a[x],end="")
    if a[x+1]=='@':
        break