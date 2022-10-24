#_________________________________________________________________________________
# Задача 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.
# Входные данные    1 2 3 5 6 7 8
# Выходные данные   4
#_________________________________________________________________________________

# with open ('list.txt','r') as data:
#     list = data.readline()
# print(list)

# list = [int(i) for i in input('Введите числа через пробел: ').split()]
# print(list)

# for i in range(len(list)-1):
#     if list[i+1] - list[i] != 1:
#         print(list[i]+1)

#_________________________________________________________________________________
# Задача 2.Напишите программу, которая подсчитает и выведет сумму квадратов 
# всех двузначных чисел, делящихся на 9 При решении задачи используйте 
# комбинацию функций filter, map, sum. Обратите внимание: на 9 должно делиться
#  исходное двузначное число, а не его квадрат.
#_________________________________________________________________________________

# num = [i for i in range(10, 100 )]
# res = sum(map(lambda x: x**2, filter(lambda x: not x % 9, num)))
# print(res)
# print(num)

#_________________________________________________________________________________
# Задача 3. Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков
# и определяет, можно ли из этих отрезков составить треугольник.

# Входные данные
# triangle(1, 1, 2)
# triangle(7, 6, 10)

# Выходные данные
# Это не треугольник
# Это треугольник
#_________________________________________________________________________________
# a, b, c = int(input()),  int(input()),  int(input())

# def triangle(a, b, c):
#     flag = False
#     if (a + b) > c and (a + c) > b and (b + c) > a:
#         flag = True
#     return 'Это треугольник' if flag else 'Это не треугольник'

# print(triangle(a, b, c))

# альтернативный вариант:

# def triangle(a, b, c):
#     return('Это не треугольник','Это треугольник')[(a + b > c) and (a + c > b) and (b + c > a)]
# print(triangle(int(input()),  int(input()),  int(input())))
#_________________________________________________________________________________
# Задача 4. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] , [1, 2, 3, 4, 6, 7], [1, 3, 4, 6, 7] и т.д.
#_________________________________________________________________________________

# list = [1, 5, 2, 3, 4, 6, 1, 7]
# list_res = [] #   => [1, 5, 6, 7]
# list_res.append(list[0])
# print(list_res)
# for i in range(1, len(list)):
#     if list[i] > list_res[-1]:
#         list_res.append(list[i])
#         print(list_res)
# print(list_res)

# list_res = []     #   => [1, 2, 3, 4]
# list_res.append(min(list))
# print(list_res)
# for i in range(len(list)):
#     if list[i] - list_res[-1] == 1:
#         list_res.append(list[i])
#         print(list_res)
# print(list_res)

# list_res = [] #   => [[1, 5, 6, 7], [1, 2, 3, 4, 6, 7], [1, 3, 4, 6, 7], [1, 4, 6, 7], [1, 6, 7], [1, 7], [1, 7]]
# for j in range(1, len(list)):
#     list_temp = [list[0]]
#     for i in range(j, len(list)):
#         if list[i] > list_temp[-1]:
#             list_temp.append(list[i]) 
#     list_res.append(list_temp)
# print(list_res)


# def filt(lst):
# # '''Функция для удления чисел, выбивающихся из последовательности'''
# start, end = lst[0], lst[-1]
# res = [start]
# for i in range(1, len(lst) - 1):
#     if start < lst[i] < end:
#         if res[-1] < lst[i]:
#             res.append(lst[i])
# return res + [end]


# sp = [1, 5, 2, 3, 4, 6, 1, 7]
# res = []
# for i in range(len(sp)):
#     for j in range(i, len(sp)):
#         if sp[j] > sp[i]:
#             res1 = sp[i:j + 1]
#             res.append(filt[res1])
#             res.append([sp[i], sp[j]])
# set_res = []
# for el in res:
#     if el not in set_res:
#         print(el)
#         set_res.append(el)