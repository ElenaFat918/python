# Задача №1 Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий
# делитель (НОД) двух чисел. Вычислите и напечатайте наибольший общий
# делитель для списка натуральных чисел. Ввод чисел продолжается до ввода пустой
# строки.
# Входные данные
#               36
#               12
#               144
#               18
# Выходные данные
#               6

from math import gcd
from functools import reduce

print('Программа нахождения наибольшего общего делителя для списка натуральных чисел')
sp = list()
print('Введите натуральные числа через Enter: ')
while(True):
    s = input().strip()
    if s == "":
        break
    sp.append(int(s))
print('Введены числа', sp)
print('Наибольший общий делитель: ' + str(reduce(gcd, sp)))