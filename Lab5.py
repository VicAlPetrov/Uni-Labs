# Вариант-21.
# Дана целочисленная матрица {Aij}i=1..n,j=1..m (n,m<=100).
# Найти столбец с наименьшей суммой элементов и заменить все элементы этого столбца этой суммой.

import numpy as np

print('Введите размерность матрицы через пробел в формате m * n, где m - число строк, а n - число столбцов')
inputList = list(map(int, input().split()))
if inputList[0] > 20 or inputList[1] > 20:
    print('Введенная размерность матрицы не соответствует условиям')
else:
    m = inputList[0]
    n = inputList[1]
inputList.clear()

print("Введите матрицу построчно")
myMatrix = np.empty((m, n), dtype=np.int_)
for i in range(m):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        myMatrix[i][j] = row[j]

sumOfFirstColumn = 0
for i in range(m):
    sumOfFirstColumn += myMatrix[i][0]

minSum = sumOfFirstColumn
numberOfMinColumn = 0
for j in range(n):
    sumOfColumn = 0
    for i in range(m):
        sumOfColumn += myMatrix[i][j]
    if sumOfColumn < minSum:
        minSum = sumOfColumn
        numberOfMinColumn = j

for i in range(m):
    myMatrix[i][numberOfMinColumn] = minSum
print(myMatrix)
