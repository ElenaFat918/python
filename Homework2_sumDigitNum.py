# Задача №1. Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 
# 6782 -> 23
# 
# 0,56 -> 11


print('Определение суммы цифр вещественного числа')
a = float(input("Введите число: "))


def sumDigit(a):
    if a < 0:
        a *= (-1)
    result = 0
    for i in str(a):
        if i != '.':
            result += int(i)
    return result
print(sumDigit(a)) # В С# писали (f'Сумма чисел равна {result(a)}')