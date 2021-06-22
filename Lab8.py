# Вариант-21.
# Во входном файле записан русский текст, содержащий не более 1000 слов.
# Если в тексте нет слов, в которых есть две одинаковые гласные буквы, то удалить из слов текста глухие согласные,
# в противном случае пpодублиpовать в словах, содержащих не более двух гласных, гласные буквы.
# Полученные слова вывести в порядке, обратном к алфавитному. Глухие согласные: пфкшстхцчщ.
# Слова вывести по одному в строке.
vowels = 'аоэеиыуёюя'
deaf_consonants = 'пфкшстхцчщ'


def there_are_two_identical_vowels(word):
    result = False
    word = word.lower()
    for i in range(len(vowels)):
        if word.count(vowels[i]) >= 2:
            result = True
    return result


def number_of_words_with_two_identical_vowels(text):
    result = 0
    for i in range(len(text)):
        if there_are_two_identical_vowels(text[i]):
            result += 1
    return result


def number_of_vowels(word):
    result = 0
    for char in word:
        for i in range(len(vowels)):
            if char == vowels[i]:
                result += 1
    return result


def get_list_from_string(word):
    list = []
    for i in range(len(word)):
        list.append(word[i])
    return list


def remove_deaf_consonants(word):
    my_list = get_list_from_string(word)
    for i in range(len(my_list)):
        if my_list[i] in deaf_consonants:
            my_list[i] = ''
    string = ''
    for i in range(len(my_list)):
        string += str(my_list[i])
    return string


def double_vowels(word):
    my_list = get_list_from_string(word)
    string = ''
    for i in range(len(my_list)):
        if my_list[i] in vowels:
            string += str(my_list[i]) * 2
        else:
            string += str(my_list[i])
    return string


file_text = open('text.txt', 'r', encoding='UTF-8')
text_string = file_text.read()
file_text.close()
text_string = text_string.replace('\n',' ')
text_list = text_string.split(' ')

if number_of_words_with_two_identical_vowels(text_list) == 0:
    for i in range(len(text_list)):
        text_list[i] = remove_deaf_consonants(text_list[i])
else:
    for i in range(len(text_list)):
        if number_of_vowels(text_list[i]) < 3:
            text_list[i] = double_vowels(text_list[i])

text_list.sort(key=lambda x: x[0], reverse=True)
for i in range(len(text_list)):
    print(text_list[i])
