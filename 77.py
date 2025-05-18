# Program 77
'''
Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them
alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''

a=input("Enter words using space : ")
b=a.split(" ");d={}
c=list(set(b))
for x in range(len(c)):
    d.update([(x,c[x])])
c=[]
for x in sorted (d,key=d.get):
    print(d[x],end=" ")