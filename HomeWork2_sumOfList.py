# Задача №3. Задайте список из n чисел последовательности (1+ 1/n )**n выведите на экран их сумму.

print('Программа задает список из n чисел последовательности (1+ 1/n )**n и выводит на экран их сумму')
n = int(input("Введите количество чисел в списке: "))

sum = 0
sp = list()


for i in range(1, n + 1):
    sum += (1+ 1/n )**n 
    i += i
    sp.append(round((1+ 1/n )**n, 2))
print(sp)


print('\nСумма чисел равна', round(sum, 2))