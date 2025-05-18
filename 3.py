'''Program 3
 Write a Python program to find the area of a triangle.'''

# AREA OF TRIANGLE

def area():
    q=int(input("\nEnter 1 for find area of triangle by sides and Enter 2 for find the area of triangle by base and height : "))

# AREA OF TRIANGLE by 3 sides
    if q==1:
        a=float(input("\nEnter length : "))
        b=float(input("\nEnter length : "))
        c=float(input("\nEnter length : "))
        s=(a+b+c)/2
        print("\nArea of triangle : ",(s*(s-a)*(s-b)*(s-c))**(1/2))
        
    
#AREA OF TRIANGLE by base and height
    elif q==2:
        a=float(input("\nEnter base : "))
        b=float(input("\nEnter height : "))
        print("\nArea of triangle : ",0.5*a*b)
            
    else:
        print("\nInvalid choice")
        area()
area()