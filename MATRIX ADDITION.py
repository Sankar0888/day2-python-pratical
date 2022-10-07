matrix1 = [[1,2,5,3]]
matrix2 = [[2,3,4,1]]
matrixsum = []
for row in range(len(matrix1)):
     matrixsum.append([])
for column in range(len(matrix[0])):
matrixsum[row].append(matrix1[row][column] + matrix2[row][column])
matrixsum = []
for row in range(len(matrix1)):
matrixsum.append([matrix1[row][column] + matrix2[row][column] for column in range(len(matrix[0]))])
matrixsum = [[matrix1[row][column] + matrix2[row][column] for column in range(len(matrix[0]))]
      for row in range(len(matrix1))]
print(matrixsum) 
