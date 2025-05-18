# Program 96
'''
Create a function that returns a base-2 (binary) representation of a base-10 (decimal)
string number. To convert is simple: ((2) means base-2 and (10) means base-10)
010101001(2) = 1 + 8 + 32 + 128.
Going from right to left, the value of the most right bit is 1, now from that every bit to
the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16,
8, 4, 2, 1).
Examples
binary(1) ➞ "1"
# 1*1 = 1
binary(5) ➞ "101"
# 1*1 + 1*4 = 5
binary(10) ➞ 1010
# 1*2 + 1*8 = 10
'''

u=int(input("If you want to convert decimal to binary, press 1 and if you want to convert binary to decimal, press 2 : "))
if u==1:
    g=int(input("\nHow many times you want to convert ? "))
    for x in range(g):
        f=int(input("\n\nEnter decimal no. to convert it into binary no. : "));h=[]
        while (f//2!=0):
            h.append(f%2)
            f=f//2
            if f==1:
                h.append(f)
        w=1
        for x in range(len(h)):
            print(h[-w],end="")
            w+=1

if u==2:        
    e=int(input("\n\nHow many times you want to convert ? "))
    for x in range(e):
        a=input("\n\nEnter binary no. to convert it into decimal no. : ");b=[]
        for x in a:
            b.append(x)
        sum=0;c=0
        for x in range(len(b)):
            sum+=(int(b[-(x+1)])*(2**c))
            c+=1
        print(sum)