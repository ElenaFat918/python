# Напишите программу, которая найдёт произведение пар чисел списка. Парой
# считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

print('Поиск произведения пар чисел из списка')

sp = [int (i) for i in ((input ("Введите значения через пробел "))).split()]
print (sp)

# spS = []

# if len(sp) % 2 == 0:
#     for i in range(0, (len(sp))//2):   
#         product = sp[i] * sp[-i-1]
#         spS.append(product)
#     print(spS)
# else:
#     for i in range(0, (len(sp) + 1) // 2):   
#         product = sp[i] * sp[-i-1]
#         spS.append(product)
#     print(spS)
def listProductPairs(sp):
    sqrt = []
    for i in range((len(sp) + 1) // 2):
        sqrt.append(sp[i] * sp[len(sp) - 1 - i])
        return sqrt
print(listProductPairs(sp))
