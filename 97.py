# Program 97
'''
Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18'''

def a(b,c,d):
    sum=0;g=[]
    for x in range(b,c+1):
        if (x%d == 0):
            g.append(x)
            sum+=x
    for x in g:
        if g[-1]==x:
            print(x,end=" = ")
        else:
         print(x,end=" + ")            
    print(sum)        
x=int(input("Enter first argument for function : "))
y=int(input("Enter second argument for function : "))
z=int(input("Enter third argument for function : "))
a(x,y,z)