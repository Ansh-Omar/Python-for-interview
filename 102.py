# Program 102
'''
Create a function that takes a list of non-negative integers and strings and return a
new list without the strings.
Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]
filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]'''

def a(b):
    c=[]
    for x in range(len(b)):
        if type(b[x])==type(1):
            c.append(b[x])
    return c
print(a([1, 2, "a", "b"]))
print(a([1, "a", "b", 0, 15]))
print(a([1, 2, "aasf", "1", "123", 123]))