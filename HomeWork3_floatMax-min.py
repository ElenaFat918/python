# Задача №3. Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части
# элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


print('Поиск разницы между максимальным и минимальным значением дробной части элементов')
sp = [1.1, 1.2, 3.1, 5, 10.01] 
print(sp)
# min = 1 
# max = 0 
# for i in sp:
#     if (i - int(i)) <= min: 
#         min = i - int(i) 
#     if (i - int(i)) >= max: 
#         max = i - int(i)   
# print('\nРазность между максимальным и минимальным значением дробной части элементов равна', round(max-min, 2))

sp_frac = [i - int(i) for i in sp if int(i) != i]   # созжаем список дроных частей
print(sp_frac)
print(max(sp_frac) - min(sp_frac))