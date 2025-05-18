# Program 134
'''
Your task is to create a Circle constructor that creates a circle with a radius provided
by an argument. The circles constructed must have two getters getArea() (PIr^2) and
getPerimeter() (2PI*r) which give both respective areas and perimeter
(circumference).
For help with this class, I have provided you with a Rectangle constructor which you
can use as a base example.
Examples
circy = Circle(11)
circy.getArea()
Should return 380.132711084365
circy = Circle(4.44)
circy.getPerimeter()
Should return 27.897342763877365
Notes
Round results up to the nearest integer'''

from math import *
class Circle:
    def area(self,n):
        print("Area of circle with radius",n,"is : ",int(pi*n*n))
    def perimeter(self,n):
        print("Perimeter of circle with radius",n,"is : ",int(2*pi*n))
circu=Circle()
circu.area(11)       
circu.perimeter(11)

print()
# ANOTHER METHOD

from math import *
class Circle:
    def __init__(self,n):
        self.n=n
    def area(self):
        print("Area of circle with radius",self.n,"is : ",int(pi*self.n*self.n))
    def perimeter(self):
        print("Perimeter of circle with radius",self.n,"is : ",int(2*pi*self.n))
circu=Circle(11)
circu.area()       
circu.perimeter()
am=Circle(4.44)
am.area()
am.perimeter()