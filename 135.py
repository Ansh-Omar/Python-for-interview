# Program 135
'''
Create a function that takes a list of strings and return a list, sorted from shortest to
longest.
Examples
sort_by_length(["Google", "Apple", "Microsoft"]) ➞ ["Apple", "Google", "Microsoft"]
sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]) ➞ ["Raphael",
"Leonardo", "Donatello", "Michelangelo"]
sort_by_length(["Turing", "Einstein", "Jung"]) ➞ ["Jung", "Turing", "Einstein"]
Notes : All test cases contain lists with strings of different lengths, so you won't have to deal
'''

def a(b):
    c={}
    for x in range(len(b)):
        c.update([(len(b[x]),b[x])])
    b=[]        
    for x in sorted(c):
        b.append(c[x])
    print(b)        
a(["Google", "Apple", "Microsoft"])        
a(["Leonardo", "Michelangelo", "Raphael", "Donatello"])
a(["Turing", "Einstein", "Jung"])