


from operator import inv


print("helo world")

# типы данны и переменные
# int, float, boolean, str, list, None

# value = None
# print(type(value))

# a = 123
# b = 1.23

# # print(type(a))
# # print(type(b))
# # value = 12334
# # print(type(value)) # посмотрим какой тип переменной будет

# s = 'helloworld'

# print(s) # вывод строки
# print(a, "-", b, "-", s)
# print('{1} - {2} - {0}'.format(a, b, s)) # интерполяция
# print(f'{a} - {b} - {s}')

# f = False
# print(f)

#СПИСКИ
# list = ['1', '2', '3', '4']
# col = ['hello', 1,2,4,5,True]
# print(list)
# print(col)


# print('Введите а')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a,' + ', b, ' = ', a+b)
# print('{} {}'.format(a, b))
# print(F'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
# ** - возведение в степень
# // - деление в целых числах
# / - деление вещественных чисел
#  
# a = 1.31231223
# b = 3
# c= round(a*b, 5)
# print(c)
# a = 3
# a += 5
# print(a)

# a = 1<4 and 5>2
# print(a)

# a = 1 !=2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5
# print(a)

# func = 1
# T = 4
# x = 123

# print(func<T>x) # тройное неравенство

# f = 1 > 2 or 4 < 6 # дизъюнкция 2-х высказываний 
#                 # - высказывание истинно тогда когда одно из высказываний истинно
# print(f)

# f = [1,2,3,4]
# # print(f)
# # print(not 2 in f)# отрицание 2 соержится в списке 

# is_odd = not f[0] % 2 # отрицание 1-цы это 0 - это ложь
# print(is_odd)

# логические ветвления : if, if-else

# Задача нахождения максимума из двух чисел

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции:
# for

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [11,2,27,4,5]
# for i in list:
#     print(i)

# r = range(10) # итератор перечисляет от 0 до 1
# for i in r:
#     print(i)

# r = range(1, 5) 
# for i in r:
#     print(i)

# r = range(1, 10, 2) #приращение на 2
# for i in r:
#     print(i)

# for i in 'qwe - rty':
#     print(i)

# text = 'сьешь ещё этих мягкихфранцузских булочек'

# help(text.istitle)

# text = 'съешь ещё этих мягких французских булок'    
# print(len(text))      # 39 
# print('ещё' in text)  # True 
# print(text.isdigit()) # False 
# print(text.islower()) # True 
# print(text.replace('ещё','ЕЩЁ')) #

# for c in text:    
#     print(c)


# text = 'съешь ещё этих мягких французских булок' print(text[0])   # c 
# print(text[1])   # ъ 
# print(text[len(text)-1])  # к 
# print(text[-5])  # б 
# print(text[:])   # 
# print(text) 
# print(text[:2])  # съ 
# print(text[len(text)-2:])  # ок 
# print(text[2:9])  # ешь ещё 
# print(text[6:-18])  # ещё этих мягких 
# print(text[0:len(text):6])  # сеикакл 
# print(text[::6])  # сеикакл 
# text = text[2:9] + text[-5] + text[:2] # ...


# Списки: введение

# numbers = [1, 2, 3, 4, 5] 
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6)) 
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10 
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:    
#     i *= 2    #в текущую переменную кладем значение, не в сам список
#     print(i)    # [20, 4, 6, 8, 10] 
# print(numbers)  # [10, 2, 3, 4, 5]

# numbers = [1, 2, 3, 4, 5] 
# print(numbers)  
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran) # привели тип range к типу list
# print(type(numbers))


# print(numbers)  
# numbers[0] = 10 
# print(f'{len(numbers)} len')   #интерполяция получаем количество элементов используя функцию len
 

# colors = ['red', 'green', 'blue']
# for e in colors:    
#     print(e)  # red green blue
# for e in colors:    
#     print(e*2)  # redred greengreen blueblue
# colors.append('gray') # добавить в конец 
# print(colors == ['red', 'green', 'blue', 'gray']) # True 
# colors.remove('red') #del colors[0] # удалить элемент
# print(colors)


#Функции  - Это фрагмент программы, используемый многократно 
 
# def function_name(x): 
    # body line 1 # . . . 
    # # body line n    
    # # optional return 
 

