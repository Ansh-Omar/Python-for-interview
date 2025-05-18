# Program 84
'''
Please write a program to generate all sentences where subject is in ["I", "You"] and
verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].'''

a = ["I", "You"]
b=["Play", "Love"]
c=["Hockey","Football"]
for x in a:
    for y in b:
        for z in c:
            print(x,y,z,sep=" ")
            
# OUTPUT
'''
I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football

'''