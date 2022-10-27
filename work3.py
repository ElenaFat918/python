# ; 1
# ; Дан список. Выведите те его элементы, которые встречаются в списке только один
# ; раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# ; списке.
# ; Входные данные
# ; Выходные данные
# ; 1 2 2 3 3 3
# ; 1

# list1 = [4, 1, 2, 2, 3, 3, 5]

# list2 = []
# for i in list1:
#      if list1.count(i) == 1: list2.append(i)    
# print(*list2)


# Дан список чисел. Выведите все элементы списка, которые больше предыдущего
# элемента.
# Входные данные
# Выходные данные
# 1 5 2 4 3
# 5
# 4

# list = [int(i) for i in input('Введите числа через пробел: ').split()]
# print(list)

# for i in range(len(list) - 1):
#     if list[i+1] > list[i]:
#         print(list[i+1])


# # Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.
# Подсказка: можно использовать модуль datetime
# import datetime 

# min_n = 10
# max_n = 100

# def get_rand():
#     return datetime.datetime.now().microsecond%10

# n = get_rand()

# print(int(len(str(min_n))))
# print(n)


# import datetime

# def rand():
#     return datetime.datetime.now().microsecond  


# print(rand())

# Задайте список. Напишите программу, которая определит, присутствует ли в
# заданном списке строк некое число.
# Входные данные
# Выходные данные
# 12
# да
# Строка1
# Строка2
# Строка3
# Строка45
# Стр12ка
# x = str(12345)
# text = ".......12345......"
# >>> x in text
# True

# # # 1
# # ist = [int(i) for i in input("Введите числа через пробел: ").split()]
# # ist = list(map(int, input("Введите числа через пробел: ").split()))
# # for i in ist:
# #     if ist.count(i) == 1:
# #         print(i)

# # # 2
# # ist = [int(i) for i in input("Введите числа через пробел: ").split()]
# # # [1 5 4 6]
# # for i in range(0, len(ist) - 1):
# #     if ist[i] < ist[i+1]:
# #         print(ist[i+1])

# # # 3
# # from datetime import datetime
# # 
# # 
# # def num_random(n):
# #     number = datetime.now().microsecond
# #     return number % n
# # 
# # 
# # (num_random(1000) + 89)

# # 4
# a = '12'
# lst = ['Строка1', 'Строка2', 'Строка3', 'Строка45', 'Стр12ка']
# count = 0
# for word in lst:
#     if a in word:
#         count += 1
# print('Да') if count > 0 else print('Нет')
