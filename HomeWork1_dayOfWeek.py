# Задача №1. Напишите программу, которая принимает на вход цифру, обозначающую 
# день недели,  и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Введите цифру, обозначающую день недели: '))
if number < 1 or number > 7:
    print('Попробуйте снова и введите цифру от 1 до 7')
elif number > 5:
    print('Это выходной!')
else:
    print('Это не выходной')