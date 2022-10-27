# Задача №4. Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в
# файле file.txt в одной строке одно число


print('Программа поиска произведения элементов на позициях, указанных в файле file.txt в одной строке одно число')

N = int(input("Введите число для создания списка из проежутка [-N, N]: "))
product = 0
sp = []

for i in range(-N,N + 1):
    sp.append(i)
print(sp)


with open('file.txt', 'w') as data:
    data.write('-1\n')
    data.write('3\n')

product = 1
path = 'file.txt'
data = open(path, 'r')   
for line in data:
    product *= sp[int(line)]
    print(f"Элемент на позиции {line} = ", sp[int(line)])
data.close()
print(f"Произведение элементов на позициях {line} = ", product)
