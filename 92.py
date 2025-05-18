# Program 92
'''
Write a function that stutters a word as if someone is struggling to read it. The first
two letters are repeated twice with an ellipsis ... and space after each, and then the
word is pronounced with a question mark ?.
Examples
stutter("incredible") ➞ "in... in... incredible?"
stutter("enthusiastic") ➞ "en... en... enthusiastic?"
stutter("outstanding") ➞ "ou... ou... outstanding?"
Hint :- Assume all input is in lower case and at least two characters long.
'''

a=input("Enter word : ")
b=a.lower()
if b.isalpha() and len(b)>1 :
    for x in range(2):
        print(b[0],b[1],"... ",sep="",end="")
    print(b,end="?")