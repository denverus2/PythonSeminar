# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def negafibonacci(n):
    fib = fibonacci(n)
    negafib = [(-1)**(i+1) * fib[i] for i in range(n, 0, -1)]
    return negafib

k = int(input('Введите число: '))
print(negafibonacci(k) + fibonacci(k))