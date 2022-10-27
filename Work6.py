#  Задача 1. Вводится список целых чисел в одну строчку через пробел. Необходимо
# оставить в нем только двузначные числа. Реализовать программу с использованием
# функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# пример - 8 11 0 -23 140 1 => 11 -23
# ___________________________________________________________________

# sp = [int(i) for i in input('Введите числа через пробел: ').split()]
# print(sp)

# res = list(filter(lambda x: 9 < x < 100, sp)) 
# res = list(filter(lambda x: len(str(x)) == 2, sp)) #  альтернативное решение
# print(res)

# ___________________________________________________________________
# Задача 2. Дан список, вывести отдельно буквы и цифры.
# a = ( ‘1’, "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')
# ___________________________________________________________________

# a = ('1','a','b','2','3','c')
# b = list(filter(lambda x: x == 'a' or x == 'b' or x =='c', a))
# c = list(filter(lambda x: x == '1' or x =='2' or x =='3', a))
# b = list(filter(lambda x: x.isalpha(), a))    #   альтернативное
# c = list(filter(lambda x: x.isalpha(), a))
# print(b)
# print(c)
# print([i for i in a if i.isdigit()])
# print([i for i in a if i.isalpha()])
# ___________________________________________________________________
# Задача 3. Преобразовать набор списков (используя функцию zip)
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
# и потом вернуть в исходное состояние
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]
# ___________________________________________________________________

# from itertools import zip_longest
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# # data = list(zip(users, ids, salary))
# # print(data)
# # users, ids, salary = zip(*data)
# # users, ids, salary = list(users), list(ids), list(salary)
# # print(users, ids, salary)
# temp = [list(i) for i in zip(users, ids, salary)]
# print(temp)
# print(list(zip(*temp)))



# temp = [list(i) for i in zip_longest(users, ids, salary, fillvalue='')]

# print(temp)
# print(list(zip(*temp)))
# for i in range(len(temp)):      #   меняем сам список, применяя фильтр как ссылку на объект
#     temp[i] = list(filter(lambda x: x, temp[i]))    #   оставили только элементы, без ''
# print(temp)

# temp = list(zip_longest(*temp))
# for i in range(len(temp)):
#     temp[i] = list(filter(lambda x: x, temp[i]))#   оставили только элементы, без 'None'
# print(temp)

# ___________________________________________________________________
# Задача 4.
# Обработка текста
# Напишите программу для обработки текста.
# На вход вашей программы подаётся многострочный текст, причём число строк заранее
# неизвестно.
# Ваша задача – пронумеровать слова в нём, начиная с нуля, а затем вывести только те
# слова, которые начинаются с большой буквы.
# Перед словом необходимо вывести номер первого вхождения этого слова в текст.
# Слова необходимо отсортировать в лексикографическом порядке. (В решении задачи
# поможет функция enumerate())
# Входные данные:
        # Ехал Грека через реку.
        # Видит Грека в реке рак.
        # Сунул в реку руку Грека.
        # Рак за руку Греку цап.
# Выходные данные
#                 4 - Видит
#                 1 - Грека
#                 17 - Греку
#                 0 - Ехал
#                 14 - Рак
#                 9 - Сунул
# ___________________________________________________________________
# Ехал Грека через реку.
# Видит Грека в реке рак.
# Сунул в реку руку Грека.
# Рак за руку Греку цап.

# text = []
# dic = {}
# for i in range(4):  #   построчно вводим данные
#     text.extend(input().replace('.', '').split())

# for i, k in enumerate(text): #   пронумеровали строки
#     if k[0].isupper():
#         if k not in dic:
#             dic[k] = i
# for k, v in sorted(dic.items()):
#     print(f'{v} - {k}')

    # альтернативное решение
text = open('6-4.txt', 'r', encoding='utf-8')
lst = list(text.read().split())
text.close()
dic = dict(enumerate(lst))
dic2 = {}
for i in dic.keys():
    if dic[i].strip(".") not in dic2.values():
        if dic[i].istitle(): dic2[i] =  dic[i]
print(dic2)
a = (sorted(dic2.items(), key=lambda x: x[1]))
print(*a)