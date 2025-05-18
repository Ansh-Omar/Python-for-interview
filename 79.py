# Program 79 
'''
Write a program that accepts a sentence and calculate the number of letters and

digits. Suppose the following input is supplied to the program:

hello world! 123

Then, the output should be:

LETTERS 10

DIGITS 3'''

a=input("Enter a sentence which must contains letters and digits : ");l=0;d=0
for x in range(len(a)):
    if a[x].isalpha():
        l+=1
    elif a[x].isdigit():
        d+=1
print("Letters : ",l)
print("Digits : ",d)