# Program 127
'''
Create a function that takes a number as an argument and returns True or False
depending on whether the number is symmetrical or not. A number is symmetrical
when it is the same as its reverse.
Examples
is_symmetrical(7227) ➞ True
is_symmetrical(12567) ➞ False
is_symmetrical(44444444) ➞ True
is_symmetrical(9939) ➞ False
is_symmetrical(1112111) ➞ True'''

def a(b):
    c=[x for x in str(b)]
    c.reverse();d=0
    for x in range(len(c)):
        d=d+(int(c[x])*(10**(len(c)-(x+1))))
    if d==b:
        print(True)
    else:
        print(False)        
    print()
a(7227)
a(12567)  
a(4444444)
a(9939)
a(1112111)