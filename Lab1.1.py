# Вариант-21. Дана последовательность целых чисел {Aj}.
# Hайти произведение неположительных чисел, наименьшее из неположительных чисел
# и номеp этого числа в последовательности.

print('Введите элементы последовательности через пробел')
my_list = list(map(int, input().split()))
new_list = my_list.copy()

my_list.sort()
if my_list[0] <= 0:
    product = 1
    for i in range(len(my_list)):
        if my_list[i] <= 0:
            product = product * my_list[i]
    print('Произведение неположительных чисел: ', product)
    minNonPositive = my_list[0]
    print('Наименьшее из неположительных чисел: ', minNonPositive)
    for i in range(len(new_list)):
        if new_list[i] == minNonPositive:
            numberOfMinNonPositive = i + 1
    print('Номер наименьшего неположительного числа: ', numberOfMinNonPositive)
else:
    print('В последовательности нет неположительных чисел')
