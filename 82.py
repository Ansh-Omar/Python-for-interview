# Program 82
'''
Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically. Suppose the following input is
supplied to the program:
Enter a sentence: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
2:2

3:2

and:1

between:1

choosing:1

new:1

or:2

python:5

read:1

to:1
'''

a=input("Enter a sentence consist of letters, digits and punctuations : ")
b=a.split();c={}
for x in b:
    x=x.strip('''`~!@#$%^&*()-=_+[]\{}|;':",./<>?''')
    x=x.lower()
    if x in c:
        c[x] = c[x] + 1
    else:
        c[x] = 1
for x in sorted(c):
    print(x," : ",c[x])
    
# OUTPUT
'''

Enter a sentence consist of letters, digits and punctuations : New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
2  :  2
3  :  2
and  :  1
between  :  1
choosing  :  1
new  :  1
or  :  2
python  :  5
read  :  1
to  :  1

'''