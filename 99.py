# Program 99
'''
Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
replace_vowels("shakespeare", "*") ➞ "shkspr*"'''

def a(b,c):
    d=['a','e','i','o','u']
    for x in b:
        if x in d:
            b=b.replace(x,c)
    print(b)
a("the aardvark","#")       
a("minnie mouse", "?")
a("shakespeare", "*")