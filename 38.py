'''Program 38
 Write a Python Program to Multiply Two Matrices.'''

# PROGRAM TO MULTIPLY TWO MATRICES

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = [];matrix2 = []

for i in range(rows):
    row1 = [];row2 = []
    for j in range(cols):
        value = int(input(f"Enter value for matrix1 [{i}][{j}]: "))
        row1.append(value)
        value = int(input(f"Enter value for matrix2 [{i}][{j}]: "))
        row2.append(value)
    matrix1.append(row1)
    matrix2.append(row2)

f=0;e=matrix1[:]
for x in range(len(matrix1)):
    for y in range(len(matrix1[x])):
        e[x][y]=matrix1[x][y]*matrix2[x][y]
    f+=1
print(e)