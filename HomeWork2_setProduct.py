# Задача №2. Напишите программу, которая принимает на вход число N и выдает набор
# произведений чисел от 1 до N.
# Пример:
# 
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Определение произведений чисел от 1 до N')
N = int(input("Введите число: "))

sp = list()
result = 1

for i in range(N) : 
    i += 1
    result *= i
    sp.append(result)
print(sp)
