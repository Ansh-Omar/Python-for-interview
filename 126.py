# Program 126
'''
Create a function that takes a string and returns True or False, depending on whether
the characters are in order or not.
Examples
is_in_order("abc") ➞ True
is_in_order("edabit") ➞ False
is_in_order("123") ➞ True
is_in_order("xyzz") ➞ True
Notes
You don't have to handle empty strings'''

def a(b):
    d=list(b);c=0;e=d[:]
    d.sort()
    for x in range(len(list(d))):
        if d[x]==e[x]:
            c+=1
    if c==len(d):
        print(True)
    else:
        print(False)        
a("abc")        
a("edabit")
a("123")
a("xyzz")