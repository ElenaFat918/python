# Задача №3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

# print('Программа, которая выведет список неповторяющихся элементов исходной последовательности')
# sp = [int (i) for i in ((input ("Введите значения через пробел "))).split()]
# print('Исходная последовательность чисел:',sp)
# spDeleteRepeat = []
# [spDeleteRepeat.append(i) for i in sp if i not in spDeleteRepeat]
# print(f"Список из неповторяющихся элементов: {spDeleteRepeat}")

sp = [1, 2, 3, 4, 2, 4]
res = []
res = [i for i in sp if sp.count(i) == 1]
# for i in sp:
#     if sp.count(i) == 1:
#         res.append(i)
print(res)