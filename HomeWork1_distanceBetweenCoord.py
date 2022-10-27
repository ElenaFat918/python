#   Задача №5. Напишите программу, которая принимает на вход координаты 
#   двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Расчет расстояния между точками в 2D пространстве')
Ax = float(input('Введите x координату 1 точки: '))
Ay = float(input('Введите y координату 1 точки: '))
Bx = float(input('Введите x координату 2 точки: '))
By = int(input('Введите y координату 2 точки: '))
import math

dist = round(math.sqrt((Bx - Ax) * (Bx - Ax) + (By - Ay)*(By - Ay)), 2)
print(dist)