# Вариант-21.
# Дана последовательность натуральных чисел {aj}j=1...n (n<=10000).
# Если в последовательности есть хотя бы одно простое число, упорядочить последовательность по невозрастаниюю.

def isprime(number):
    if number <= 1:
        return False
    i = 2
    while i ** 2 <= number:
        if number % i == 0:
            return False
        i += 1
    return True


print('Введите элементы последовательности через пробел')
my_list = list(map(int, input().split()))

primeNumbersCounter = 0
for i in range(len(my_list)):
    if isprime(my_list[i]):
        primeNumbersCounter += 1

if primeNumbersCounter != 0:
    my_list.sort(reverse=True)
print(my_list)
