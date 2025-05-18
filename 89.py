# Program 89
'''
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in
comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
8
Then, the output of the program should be:
0,1,1,2,3,5,8,13'''

a=int(input("Enter limit : "))
b=[0,1]
[b.append(b[-1]+b[-2]) for x in range (2,a)]
print(b)