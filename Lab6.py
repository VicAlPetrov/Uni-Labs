# Вариант-21.
# Дана последовательность натуральных чисел {Aj}j=1...n (n<=10000).
# Удалить из последовательности числа, все цифры которых различны, а среди оставшихся продублировать числа,
# произведение цифр которых кратно 14.

def get_digits(number):
    digits_list = []
    while number > 0:
        digit = number % 10
        digits_list.append(digit)
        number = number // 10
    return digits_list[::-1]


def there_are_identical_digits(number):
    result = False
    digits_list = get_digits(number)
    if len(digits_list) == 1:
        result = True
    for i in range(len(digits_list) - 1):
        for j in range(i + 1, len(digits_list)):
            if digits_list[i] == digits_list[j]:
                result = True
    return result


def product_of_digits(number):
    my_list = get_digits(number)
    product = 1
    for i in range(len(my_list)):
        product = product * my_list[i]
    return product


print('Введите элементы последовательности через пробел')
my_list = list(map(int, input().split()))

for x in my_list[:]:
    if not there_are_identical_digits(x):
        my_list.remove(x)
for x in my_list[:]:
    if product_of_digits(x) % 14 == 0:
        my_list.insert(x + 1, x)
print(my_list)
