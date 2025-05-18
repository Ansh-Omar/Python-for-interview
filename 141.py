# Program 141
'''
Create a function that takes a string as input and capitalizes a letter if its ASCII code
is even and returns its lower case version if its ASCII code is odd.
Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"
ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"
ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."
'''
def a(b):
    for x in b:
        if ord(x)%2==0:
            b=b.replace(x,x.upper())
        else :
            b=b.replace(x,x.lower())
    print(b)            
a("to be or not to be!")    
a("THE LITTLE MERMAID")
a("Oh what a beautiful morning.")