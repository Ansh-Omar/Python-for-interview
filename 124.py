# Program 124
'''
A group of friends have decided to start a secret society. The name will be the first
letter of each of their names, sorted in alphabetical order. Create a function that takes
in a list of names and returns the name of the secret society.
Examples
society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"
society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"
society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])'''

def a(b):
    c=[]
    for x in b:
        c.append(x[0])
    for x in sorted(c):
        print(x,end="")
    print()        
a(["Adam", "Sarah", "Malcolm"])
a(["Harry", "Newt", "Luna", "Cho"])
a(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])