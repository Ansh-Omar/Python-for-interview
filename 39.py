'''Program 39
 Write a Python Program to Transpose a Matrix.'''

# PROGRAM TO TRANSPOSE A MATRIX

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = []

for i in range(rows):
    row1 = []
    for j in range(cols):
        value = int(input(f"Enter value for matrix1 [{i}][{j}]: "))
        row1.append(value)
    matrix1.append(row1)

print(matrix1);x=0
e=[]
for x in range(cols):
    r2=[]
    for y in range(rows):
        r2.append(matrix1[y][x])
    e.append(r2)
print()
print(e)