# Program 80
'''
A website requires the users to input username and password to register. Write a
program to check the validity of password input by users. Following are the criteria
for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will
check them according to the above criteria. Passwords that match the criteria are to
be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1'''

a=input("Enter various password using comma : ")
b=a.split(",");d=['$','#','@']
e=[]
for x in range(len(b)):
    if 6<=(len(b[x]))<=12:
        c1=0;c2=0;c3=0;c4=0
        for y in range(len(b[x])):
            if b[x][y].isalpha():
                if b[x][y].isupper():
                    c1+=1
                elif b[x][y].islower():
                    c2+=1
            elif b[x][y].isdigit():
                c3+=1
            elif b[x][y] in d:
                c4+=1
        #print(c1,c2,c3,c4)
        if c1>0 and c2>0 and c3>0 and c4>0:
            e.append(b[x])            
for x in e:
    print(x)