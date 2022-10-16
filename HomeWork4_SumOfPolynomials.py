# Задача №5. Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.
import re
print('Программа, формирующая файл, содержащий сумму многочленов')

with open ('polynomialFirst.txt','r') as data:
    polynomialFirst = data.readline()
print(f"Первый многочлен {polynomialFirst}") #  84x^2+11x^1+87x^0

with open('polynomialSecond.txt', 'r') as data:
    polynomialSecond = data.readline()
print(f"Второй многочлен {polynomialSecond}") # 27x^3+13x^2+82x^1+97x^0


for i in polynomialFirst:                      
    degreeFirst = polynomialFirst.count('+')
print('Степень первого многочлена', degreeFirst)

for i in polynomialSecond:                      
    degreeSecond = polynomialSecond.count('+')
print('Степень второго многочлена', degreeSecond)

def selectKoef(polynomial):
    list = re.findall('[0-9]+', polynomial) # нашли все числа с 0 до 9 в polynomial
    list = [int(i) for i in list]   # список строк переводим в список целых чисел
    listKoef = []
    for i in range(0, len(list), 2):    #записываем коэффициенты  с четным индексом
        listKoef.append(list[i])
    return listKoef

koefFirst = selectKoef(polynomialFirst)
print('Список коэффициентов первого многочлена:', koefFirst)

koefSecond = selectKoef(polynomialSecond)
print('Список коэффициентов второго многочлена:',koefSecond)

if degreeFirst > degreeSecond:
    maxDegree = degreeFirst #   максимальная степень в многочленах
    for i in range(degreeFirst - degreeSecond):
        koefSecond.insert(i, 0)
else:
    maxDegree = degreeSecond
    for i in range(degreeSecond - degreeFirst):
        koefFirst.insert(i, 0)
print('Списки тождественных по размеру коэффициентов многочленов:', koefFirst, koefSecond)

sumKoef = []
for i in range(len(koefFirst)):
    sumKoef.append(koefFirst[i] + koefSecond[i])
print('Список суммы коэфициентов многочленов:', sumKoef)

x = 'x' 
member = []
for i in sumKoef: 
    i = str(i) + str(x) + '^' + str(maxDegree) #Переводим коэффициет в строку и соединяем его с х^k в один элемент i
    member.append(i) 
    maxDegree -= 1
sumPolynomial = '+'.join(member)    #Слияние элементов в строку
print('Сумма многочленов:', sumPolynomial)

with open('SumPolinomials.txt', 'w') as data:
    data.write(sumPolynomial)