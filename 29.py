''' Program 29
 Write a Python Program to calculate your Body Mass Index.
 Body Mass Index (BMI) is a measure of body fat based on an individual's weight and
 height. It is commonly used as a screening tool to categorize individuals into different weight
 status categories, such as underweight, normal weight, overweight, and obesity.
 The BMI is calculated using the following formula:
 BMI = Weight (kg) upon Height (m) square
 Alternatively, in the imperial system:
 BMI = [ Weight (lb) upon Height (in) square ] × 703
 
 
 BMI provides a general indication of body fatness but does not directly measure body fat or
 distribution. It is widely used in public health and clinical settings as a quick and simple tool
 to assess potential health risks associated with weight. Different BMI ranges are associated
 with different health categories, but it's important to note that BMI has limitations and does
 not account for factors such as muscle mass or distribution of fat'''

# BODY MASS INDEX

a=float(input("Enter weight in kilogram : "))
b=float(input("Enter your height in metres : "))
c=(a/(b**2))
print("\nYour Body Mass Index is",c)
if c<18.5:
    print("\nYou are underweight.")
elif c>=18.5 and c<24.99:
    print("\nYou are normal.")
elif c>=25 and c<29.99:
    print("\nYou are overweight.")
else:
    print("\nYou are obese.")