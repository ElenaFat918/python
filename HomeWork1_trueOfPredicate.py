#  Задача №2 Напишите программу для проверки истинности утверждения 

#   ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z         для всех значений предикат.

print('Программа проверки истинности утверждения для всех значений предикат')
for X in [0, 1]:
    print(X)
    for Y in [0, 1]:
        print(Y)
        for Z in [0, 1]:
            print(Z)
            print(f'Подставим следущие значения: X = {X}, Y = {Y}, Z = {Z}')
            leftComment = not (X or Y or Z)
            writeComment = (not X) and (not Y) and (not Z)
            if leftComment == writeComment:
                print(f'Результат проверки: {leftComment} = {writeComment} - Верно \n')
            else:
                print(f'Результат проверки: {leftComment} = {writeComment} - Не верно \n')