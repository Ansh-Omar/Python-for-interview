# Program 87
'''
Please write a program using generator to print the numbers which can be divisible
by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70'''

class a:
    def b(n):
        for x in range(n+1):
            if (x%5==0) and (x%7==0):
                yield x
    x=int(input("Enter value for n : "))
    c=b(x)    
    for x in c:
        print(x,end=",")