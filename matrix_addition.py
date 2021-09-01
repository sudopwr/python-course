matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [1,1,1],
    [2,2,2],
    [3,3,3]
]

matrix3 = []

for row in range(3):
    newList = []
    for col in range(3):
        add = matrix1[row][col] + matrix2[row][col]
        newList.append(add)
    
    matrix3.append(newList)


print(matrix3)
