# Даны три целых числа. Определите, сколько среди них совпадающих. Программа
# должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0
# (если все числа различны).
#   Входные данные        Выходные данные
#   10                      2
#   5
#   10


# a = int(input('1 '))
# b = int(input('2 '))
# c = int(input('3 '))
# arr = [a, b, c]
# count = [0, 0, 0]
# for i in range(3):
#     for j in range(3):
#         if arr [i] == arr [j]:
#             count [i] += 1
# k = max(count)
# if k == 1:
#     print(0)
# else:
#     print(k)

# print("Введите три числа")
# a = [0]*3
# y =0
# for i in range (3):
#     print("Введите",i,'число')
#     a[i] = int(input())
# if a[0] == a [1] == a[2]:
#     print("Совпадений:",3)
# elif (a[0] == a [1] or a[1]== a[2]) or (a[0] == a [2] or a[0]== a[1]):
#     print("Совпадений:",2)
# else:
#     print("Совпадений:",0)

# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#     print(0)


# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# c = int(input("Введите число: "))

# def GetNum(a, b, c):
#     if a == b == c:
#         return 3
#     if a == b or b==c or a==c:
#         return 2
#         return 0

# print(GetNum(a,b,c))


# Даны два целых числа A и В, A>BA>B. Выведите все нечётные числа от A до B
# включительно, в порядке убывания. В этой задаче можно обойтись без инструкции
# if.
# Входные данные    
# 7
# 
# 1
# Выходные данные
# 7 5 3 1

# A = int(input('Введите число A '))

# B = int(input('Введите число B '))

# A=A-(A+1)%2

# for i in range(A,B-1,-2):
#    print(i)
# # ********************************88
# a = int(input())
# b = int(input())
# for i in range(a - (a + 1) % 2, b - 1, -2):
#     print(i, end=' ')

# Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

#N = int(input('Введите число N '))
#for i in range(N):
#    print((-3)**i)

# Напишите программу, которая проверяет пятизначное число на палиндром.

# N = int(input('Введите число N '))
# Number1 = int(N / 10000)
# Number2 = int(N / 1000 - Number1 * 10)
# Number4 = int((N % 100) /10)
# Number5 = int(N%10)

# if(Number1 == Number5 and Number2 == Number4):
#    print("Да")
# else:
#    print("Нет")

# number = '12321'
# palindrome = True
# for i in range(len(number) // 2):
#     if number[i] != number[-i-1]:
#         palindrome = False
#         break
# if palindrome:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# Удалить вторую цифру трёхзначного числа.

# N = int(input('Введите трёхзначное число N '))
# Number1 = int(N / 100)
# Number3 = int(N % 10)
# print(Number1,Number3)

# number = int(123)
# n1 = number // 100
# n2 = number % 10
# res = n1 * 10 + n2
# print(res)


# number = list(str(123))
# del number[1]
# print(''.join(number))


# Напишите программу, в которой пользователь будет задавать две строки, а
# программа - определять количество вхождений одной строки в другой.

# string = 'cccchjkccc'
# find = 'cc'
# # print(string.count(find))
# count = 0
# i = 0
# while i < len(string):
#     if string[i:i + len(find)] == find:
#         count += 1
#         i += len(find)
#     else:
#         i += 1
#         print(count)