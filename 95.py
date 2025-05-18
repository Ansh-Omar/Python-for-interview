# Program 95
'''
Given the side length x find the area of a hexagon.
Examples
area_of_hexagon(1) ➞ 2.6
area_of_hexagon(2) ➞ 10.4
area_of_hexagon(3) ➞ 23.4'''

a=int(input("Enter length of hexagon : "))
print("Area of hexagon of side",a,"is : ",round((((3*(3**(1/2)))/2)*(a**2)),1))