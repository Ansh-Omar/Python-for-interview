# Program 88
'''
Please write a program using generator to print the even numbers between 0 and n in
comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10'''

class a:
    def b(n):
        for x in range(n+1):
            if x % 2 == 0:
                yield x
    p=int(input("Enter value for n : "))
    c=b(p)
    for x in c:
        print(x,end=",")