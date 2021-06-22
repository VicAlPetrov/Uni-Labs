# Вариант-21. Дана последовательность целых чисел {Aj}.
# Hайти произведение неположительных чисел, наименьшее из неположительных чисел
# и номеp этого числа в последовательности.

print('Введите элементы последовательности через пробел')
my_list = list(map(int, input().split()))

minNonPositive = 1
product = 1
countOfNonPositive = 0
for i in range(len(my_list)):
    if my_list[i] <= 0:
        countOfNonPositive += 1
        product = product * my_list[i]
        if my_list[i] < minNonPositive:
            minNonPositive = my_list[i]
            numberOfMinNonPositive = i
if countOfNonPositive == 0:
    print('В последовательности нет неположительных чисел')
else:
    print('Произведение неположительных чисел: ', product)
    print('Наименьшее из неположительных чисел: ', minNonPositive)
    print('Номер наименьшего неположительного числа: ', numberOfMinNonPositive + 1)
