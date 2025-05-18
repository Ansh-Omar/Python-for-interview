# Program 91
'''
Define a class named Shape and its subclass Square. The Square class has an init
function which takes a length as argument. Both classes have an area function which
can print the area of the shape where Shape's area is 0 by default.
'''

class Shape :
    def area(self):
        return 0
class Square(Shape):
    def __init__(self):
        a=int(input("Enter the length of square : "));self.a=a
    def area(self):
        print(f"Area of square of length {self.a} is {self.a**2}.") 
a=Square()
a.area()