# Задача №5. Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


def Fibonacci(num): 
     if num in [1, 2]:                        
         return 1 
     else: 
         return Fibonacci(num-1) + Fibonacci(num-2) 
  
def NegaFibonacci(num): 
     if num == 1:                        
         return 1 
     elif num == 2:                        
         return -1 
     else: 
         num1, num2 = 1, -1 
         for i in range(2, num): 
             num1, num2 = num2, num1 - num2 
         return num2 
print('Программа, составляющая список чисел Фибоначчи, в том числе для отрицательных индексов.')  
sp = [0] 
k = int(input('Введите число k: ')) 
for i in range(1, k + 1): 
     sp.append(Fibonacci(i)) 
     sp.insert(0, NegaFibonacci(i)) 
print(f'Для k = {k} список будет выглядеть так:\n', sp)
# 
# n = int(input("Введите  число:\n"))
# fib = [0, 1]
# for i in range(2, n + 1):
#     fib.append(fib[-1] + fib[-2])
# for i in range(n):
#     fib = [fib[1] - fib[0]] + fib
# print(fib)