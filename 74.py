# Program 74

# WRITE A PROGRAM THAT CALCULATES AND PRINTS THE VALUE ACCORDING TO THE GIVEN FORMULA : 
'''
Q = Square root of ((2CD)/H)
Following are the fixed values of C and H : 
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma - seperated sequence.
Example : 
Let us assume the following comma seperated input sequence is given to the program : 
100 , 150 , 180
The output of the program should be : 
18,22,24'''

a = (input("Enter various value for D using comma : "))
b=a.split(',')
for x in b:
    d=int(x)
    print("Q for ",d," = ",int(((2*50*d)/30)**(1/2)))