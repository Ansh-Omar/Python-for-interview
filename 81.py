# Program 81
'''
Define a class with a generator which can iterate the numbers, which are divisible by
7, between a given range 0 and n.'''

class a:
    def b(n):
        for x in range(n+1):
            if x%7==0:
                yield x
    d=int(input("Enter limit : "))            
    c=b(d)
    for x in c:
        print(x)