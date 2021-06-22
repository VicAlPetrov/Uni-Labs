# Вариант-21.
# Дана целочисленная матрица {Aij}i=1...n;j=1..n , n<=100.
# Если не в каждой строке матрицы есть простые числа,
# заменить диагональные элементы матрицы на наименьшие элементы соответствующих строк.
# Использовать подпрограммы!

import numpy as np


def is_prime(number):
    if number <= 1:
        return False
    i = 2
    while i ** 2 <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def row_has_prime(row):
    prime_counter = 0
    for i in range(len(row)):
        if is_prime(row[i]):
            prime_counter += 1
    if prime_counter != 0:
        return True
    else:
        return False


def min_in_row(row):
    min = row[0]
    for i in range(len(row) - 1):
        for j in range(i +1, len(row)):
            if row[j] <= row[i]:
                min = row[j]
    return min


print('Введите размерность матрицы')
number = int(input())
if number > 100 or number < 1:
    print('Введенная размерность матрицы не соответствует условиям')
else:
    m = number
    n = number

print("Введите матрицу построчно")
myMatrix = np.empty((m, n), dtype=np.int_)
for i in range(m):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        myMatrix[i][j] = row[j]

for i in range(m):
    prime_row_counter = 0
    for j in range(n):
        if row_has_prime(myMatrix[j]):
            prime_row_counter += 1

if prime_row_counter != n:
    for j in range(n):
        myMatrix[j][j] = min_in_row(myMatrix[j])

print(myMatrix)