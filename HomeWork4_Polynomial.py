# Задача №4. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.

# Пример:   k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


print('Программа, формирующая случайный список коэффициентов многочлена и записывающая в файл многочлен степени k')
k = int(input('Введите натуральную степень k '))
sp = []

import random

for i in range(0, k+1):
    i = random.randint(0, 100)
    sp.append(i)
print('Получился следующий список коэффициентов многочлена: ', sp)
x = 'x' 
member = []
for i in sp: 
    i = str(i) + str(x) + '^' + str(k) 
    member.append(i) 
    k -= 1
polynomial = '+'.join(member)
print('Сформирован и записан в файл listOfCoefficients.txt многочлен', polynomial)
with open('listOfCoefficients.txt', 'w') as data:
    data.write(polynomial)

# def create_formula(factors):
#     k = len(factors) - 1
#     res = ""
#     for i in range(0, len(factors)):
#         if i == len(factors) - 1:
#             res += f'{factors[i]}'
#         elif k == 1:
#             res += f'{factors[i]}x + '
#         else:
#             res += f'{factors[i]}x^{k} + '
#         k -+ 1
#     return res

# print(create_formula([2, 3, 4]))

# def polinome(k, file_nae):
#     factors = [radint(1, 101) for i in range(0, k + 1)]
#     res = create_formula(factors)
#     with open(file_name, 'w', encoding = 'utf-8') as f:
#         f.write(' '.join([str(i) for i in factors[::-1]]) + '\n')
#         f.write(res)

# polinome(3, 'file1.txt')
# polinome(3, 'file2.txt')