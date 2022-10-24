# Задача №2. Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

# print('Программа, составляющая список простых множителей числа N')
# num = int(input("Введите натуральное число N: "))
# i = 2 
# sp = []
# N = num
# while i <= num:
#     if num % i == 0:
#         sp.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Для простых множителей числа N = {N} получился список : {sp}")


def prime(number):
    res = []
    d =2
    while d <= number:
        if number % d == 0:
            res.append(d)
            number //= d
        else:
            d += 1
    if number > 1:
        res.append(number)
    return res
print(prime(200))