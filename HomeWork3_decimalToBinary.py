# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print('Программа преобразования десятичнго числа в двоичное')
# binaryNum = "" 
# decimalNum = int(input("Введите двоичное число:\n")) 
# while decimalNum != 0: 
#      binaryNum = str(decimalNum%2) + binaryNum 
#      decimalNum //=2 
# print(binaryNum)

res = ''
n = int(input("Введите двоичное число:\n"))
while n > 0:
     res = str(n % 2) + res
     n //= 2
print(res)


