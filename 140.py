# Program 140
'''
Write a function, that replaces all vowels in a string with a specified vowel.
Examples
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"
vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
Notes
All words will be lowercase. Y is not considered a vowel.'''

def a(b,c):
    d=["a","e","i","o","u"]
    for x in b:
        if x in d:
            b=b.replace(x,c)
    print(b)            
a("apples and bananas", "u")
a("cheese casserole", "o")
a("stuffed jalapeno poppers", "e")