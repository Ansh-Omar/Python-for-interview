# Program 112
'''
Create a function that takes a list of strings and integers, and filters out the list so
that it returns a list of integers only.
Examples
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
filter_list(["A", 0, "Edabit", 1729, "Python", 1729]) ➞ [0, 1729]
filter_list(["Nothing", "here"]) ➞ []'''

def a(b):
    c=[]
    for x in b:
        if type(x)==type(1):
            c.append(x)
    print(list(set(c)))
a([1, 2, 3, "a", "b", 4])
a(["A", 0, "Edabit", 1729, "Python", 1729])
a(["Nothing", "here"])