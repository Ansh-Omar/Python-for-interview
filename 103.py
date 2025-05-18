# Program 103
'''
The "Reverser" takes a string as input and returns that string in reverse order, with
the opposite case.
Examples
reverse("Hello World") ➞ "DLROw OLLEh"
reverse("ReVeRsE") ➞ "eSrEvEr"
reverse("Radar") ➞ "RADAr" '''

def a(b):
    c=[]
    for x in range(len(b)):
        if b[x].islower()==True:
            c.append(b[x].upper())
        elif b[x].isupper()==True:
            c.append(b[x].lower())
        else:
            c.append(b[x])
    d=-1
    for x in range(len(c)):
        print(c[d],end="")
        d-=1
    print()
a("Hello World")
a("ReVeRsE")
a("Radar")