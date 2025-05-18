# Program 119
'''
Create a function that takes a string and returns a string with its letters in
alphabetical order.
Examples
alphabet_soup("hello") ➞ "ehllo"
alphabet_soup("edabit") ➞ "abdeit"
alphabet_soup("hacker") ➞ "acehkr"
alphabet_soup("geek") ➞ "eegk"
alphabet_soup("javascript") ➞ "aacijprstv"'''

def a(b):
    c=[x for x in b]
    for x in sorted(c):
        print(x,end="")
    print()        
a("hello")
a("edabit")
a("hacker")
a("geek")
a("javascript")