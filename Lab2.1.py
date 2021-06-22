# Вариант-21. Дана целочисленная матрица {Aij}i=1,...,n;j=1,...,m (n,m<=20).
# Найти минимум из наибольших элементов строк.
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

listOfMaximums = []
for i in range(m):
    maxElemOfTheRow = myMatrix[i][0]
    for j in range(1, n):
        if myMatrix[i][j] > maxElemOfTheRow:
            maxElemOfTheRow = myMatrix[i][j]
    listOfMaximums.append(maxElemOfTheRow)

minOfMaximums = min(listOfMaximums)

print(myMatrix)
print('Минимум из наибольших элементов строк равен: ', int(minOfMaximums))