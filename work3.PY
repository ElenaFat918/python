# Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя используйте пробел.

# sp = '1 4 76 33 0 -4'
# print(sp)
# sp = sp.split()
# print( 'max = ', max(sp), 'min = ', min(sp))


# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного
# уравнения
# 2) с помощью дополнительных библиотек Python


# # 1)
# a, b, c = 1, 2, 1
# D = b ** 2 - (4 * a * c)
# if D > 0:
#     x1 = (-b + D**0.5) / (2 * a)
#     x2 = (-b - D**0.5) / (2 * a)
#     print(round((x1), 3), round((x2), 3))
# elif D == 0:
#     x = -(b / (2 * a))
#     print(round((x), 3))
# else:
#     print('Вещественных корней нет')


# # 2)
# from math import sqrt

# a, b, c = 1, 2, 1
# D = b ** 2 - (4 * a * c)
# if D > 0:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - sqrt(D)) / (2 * a)
#     print(round((x1), 3), round((x2), 3))
# elif D == 0:
#     x = -(b / (2 * a))
#     print(round((x), 3))
# else:
#     print('Вещественных корней нет')

# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.


# a = int(input('Введите первое число '))
# b = int(input('Введите второе число '))
# if a > b:
#     num = a
# else:
#     num = b
# trigger = True
# while trigger == True:
#     if (num % a) == 0 and (num % b) == 0:
#         trigger = False
#     else:
#         num += 1
# print(num)

# В единственной строке записан текст. Для каждого слова из данного текста
# подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца
# строки.

# Входные данные      one two one tho three
# Выходные данные     0 0 1 0 0

# text = 'one two one tho three'
# text = text.split()
# double = {}
# for i in text:
#     if i in double:
#         double[i] += 1
#         print(double[i], end=' ')
#     else:
#         double[i] = 0
#         print(double[i], end=' ')
# for key in double:
#     if double[key] > 0:
#         print(key, 'встречается более 1 раза')


# 5
# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к
# парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.
# Входные данные

# 3
#  Hello Hi
# Bye Goodbye
# # List Array
# # Goodbye

# # Выходные данные
# # Bye
# # [11:22] ключ:элемент

# vocab = {}
# text = open ('4-5.txt','r')
# for line in text:
#         a = line.split()
#         if len(a) == 2:
#             vocab[a[0]] = a[1]
#         if len(a) == 1:
#             word = a[0]
# text.close()
# print (f"Ищем синоним для слова: {word}")
# for k, v in vocab.items(): 
#     if v == word:
#         print(k)
#     if k == word:
#         print(v)


# Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите
# слово, которое в этом тексте встречается чаще всего. Если таких слов несколько,
# выведите то, которое меньше в лексикографическом порядке.
# Входные данные
# 1
# apple orange banana banana orange

# Выходные данные
# banana

# vocab = {}
# text = open('4-6.txt', 'r')
# a = (text.read()).split()
# text.close()
# for i in range(1, len(a)):
#     if a[i] not in vocab:
#         vocab[a[i]] = 1
#     else:
#         vocab[a[i]] += 1
# lst = []

# for k, v in vocab.items():
#     if v == (max(vocab.values())):
#         lst.append(k)

# lst.sort()
# print(lst[0])

# sp = ['rr', 'tt','tt', 'tt', 'tt']
# d = {}
# # заполнение словаря
# for i in sp:
#     d[i] = d.get(i, 0) + 1
# print(list(d.keys()))
# print(list(d.values()))
# print(d.items())
# # перебор словаря
# for key, val in d.items():
#     print(key, val)
# # сортировка словаря по значениям (по убыванию)
# print(dict(sorted(d.items(), key=lambda x: -x[1])))
