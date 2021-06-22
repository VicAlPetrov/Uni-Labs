#Вариант-21. Дана последовательность целых чисел {Aj}.
#Hайти произведение неположительных чисел, наименьшее из неположительных чисел и номеp этого числа в последовательности.

print('Введите элементы последовательности через пробел')
my_tuple = tuple(map(int, input().split()))

new_tuple = tuple(sorted(my_tuple))

if new_tuple[0] <= 0:
    product = 1
    for i in range(len(my_tuple)):
        if my_tuple[i] <= 0:
            product = product * my_tuple[i]
    print('Произведение неположительных чисел: ', product)
    minNonPositive = new_tuple[0]
    print('Наименьшее из неположительных чисел: ', minNonPositive)
    for i in range(len(my_tuple)):
        if my_tuple[i] == minNonPositive:
            numberOfMinNonPositive = i + 1
    print('Номер наименьшего неположительного числа: ', numberOfMinNonPositive)

else:
    print('В последовательности нет неположительных чисел')
