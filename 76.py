# Program 76
'''
Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''

a=input("Enter words using comma : ");g=a.lower()
b=g.split(',');c=[];d={}
for x in range(len(b)):
    d.update([(x+1,b[x])])
for x in sorted(d,key = d.get):
    c.append(d[x])
for x in c:
    if x==c[-1]:
        print(x)
    else:
        print(x,end=",")