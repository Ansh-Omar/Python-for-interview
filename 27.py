''' Program 27
 Write a Python Program to Display Fibonacci Sequence Using Recursion.
 Fibonacci sequence:
 The Fibonacci sequence is a series of numbers in which each number is the sum of the two
 preceding ones, usually starting with 0 and 1. In mathematical terms, it is defined by the
 recurrence relation ( F(n) = F(n-1) + F(n-2) ), with initial conditions ( F(0) = 0 ) and ( F(1) = 1
 ). The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. The Fibonacci sequence has
 widespread applications in mathematics, computer science, nature, and art.'''

# DISPLAY FIBONACCI SEQUENCE USING RECURSION

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
a=int(input("Enter limit : "))
print("Fibonacci sequence : \n")
for x in range(a):
    print(fib(x))