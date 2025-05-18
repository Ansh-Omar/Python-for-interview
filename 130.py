# Program 130
'''
Create a function that sorts a list and removes all duplicate items from it.
Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
setify([4, 4, 4, 4]) ➞ [4]
setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]
setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]'''

def a(b):
    c=[]
    for x in set(sorted(b)):
        c.append(x)
    print(c)
a([1,3,3,5,5])
a([4, 4, 4, 4])
a([5, 7, 8, 9, 10, 15])
a([3, 3, 3, 2, 1])