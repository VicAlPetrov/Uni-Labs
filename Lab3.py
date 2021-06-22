# Вариант-21.
# Ввести последовательность натуральных чисел {Aj}j=1...n (n<=1000).
# Упорядочить последовательность по невозрастанию первой цифры числа,
# числа с одинаковыми первыми цифрами дополнительно упорядочить по невозрастанию суммы цифр числа,
# числа с одинаковыми первыми цифрами и одинаковыми суммами цифр дополнительно упорядочить по невозрастанию самого числа

def getfirstdigit(number):
    while number > 0:
        if number < 10:
            return number
        else:
            number = number // 10
    return number


def sumofdigits(number):
    _sum = 0
    while number > 0:
        _sum += number % 10
        number = number // 10
    return _sum


print('Введите элементы последовательности через пробел')
my_list = list(map(int, input().split()))

print(sorted(my_list, key=lambda element: (sumofdigits(element), getfirstdigit(element), element), reverse=True))
