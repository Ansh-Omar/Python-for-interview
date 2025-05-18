''' Program 48
 Write a Python program to print all pronic numbers between 1 and 100.'''

# PRONIC NUMBER BETWEEN 1 AND 100

'''A pronic number also known as an oblong number or rectangular number,is a type of figurate number that represents a rectangle.It is the product of two consecutive integers, n and (n+1).
Example : 2 = 1*2 , 6 = 2*3 , 12 = 3*4 , 20 = 4*5'''

'''EXAMPLES : 2 , 6 , 12 , 20 , 30 , 42 , 56 , 72 , 90 , 110 , 132 , 156 , 182 , 210 , 240 , 272 , 306 , 342 , 380 , 420 , 462 , 506 , 552 , 600 , 650 , 702 , 756 , 812 , 870 , 930 , 992 , 1056 , 1122 , 1190 , 1260 , 1332 , 1406 , 1482 , 1560 , 1640 , 1722 , 1806 , 1892 , 1980 , 2070 , 2162 , 2256 , 2352 , 2450 , 2550 , 2652 , 2756 , 2862 , 2970 , 3080 , 3192 , 3306 , 3422 , 3540 , 3660 , 3782 , 3906 , 4032 , 4160 , 4290 , 4422 , 4556 , 4692 , 4830 , 4970 , 5112 , 5256 , 5402 , 5550 , 5700 , 5852 , 6006 , 6162 , 6320 , 6480 , 6642 , 6806 , 6972 , 7140 , 7310 , 7482 , 7656 , 7832 , 8010 , 8190 , 8372 , 8556 , 8742 , 8930 , 9120 , 9312 , 9506 , 9702 , 9900'''

x = int(input("Enter starting range : "))
y = int(input("Enter last range : "))
for a in range(x,y+1):
    b=a;l=[]
    for z in range (1,a+1):
        c=a%z
        if b==2 and c==0 :
            l.append(z)
        elif c==0 and z!=1 :
            l.append(z)
    #print(l)
    #print(len(l))
    m=len(l)
    f=0;g=1
    if m>1:
        while((m-1)>0):
            k = l[f]-l[g]
            if k == -1 :
                if l[f]*l[g]==b:
                    print(b,"is pronic number.\n")
                    break
            f=g;g+=1
            m-=1
        else :
            print(b,"is not pronic number.\n")
    else:
        print(b,"is not pronic number.\n")