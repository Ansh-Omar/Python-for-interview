# Program 106'''
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
Move all the 1s to the end of the array.
move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]'''

def a(b,c):
    d=[];f=[]
    for x in range(len(b)):
        if b[x]==c:
            d.append(b[x])
        elif b[x]!=c:
            f.append(b[x])
    f.extend(d)
    print(f)
a([1, 3, 2, 4, 4, 1], 1)
a([7, 8, 9, 1, 2, 3, 4], 9)
a(["a", "a", "a", "b"], "a")