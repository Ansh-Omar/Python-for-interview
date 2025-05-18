# Program 100
'''
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1'''

q=int(input("How many times you want to calculate ? "))
for x in range(q):
    def fact(a):
        if a<=1:
            return  a
        else:
            return a*fact(a-1)
    b=int(input("\nEnter number : "));print()
    print(fact(b))