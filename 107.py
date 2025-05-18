# Program 107
'''
Question1
Create a function that takes a string and returns a string in which each character is
repeated once.
Examples
double_char("String") ➞ "SSttrriinngg"
double_char("Hello World!") ➞ "HHeelllloo WWoorrlldd!!"
double char("1234! ") ➞ "11223344!! "'''

def a(b):
    for x in b:
        print(x,x,sep="",end="")
    print()
a("String")        
a("Hello World!")
a("1234! ")