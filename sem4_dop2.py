# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.


def dec_to_other(num, sist):
    if num == 0:
        return "0"
    out = []
    while num:
        out.append(int(num % sist))
        num //= sist
    out = out[::-1]
    return "".join(map(str, out))


# Пример использования функции
n = int(input("Введите число в десятичной: "))

print(dec_to_other(n, 2))
print(dec_to_other(n, 8))

# Проверка с помощью встроенных функций bin и oct
print(f"Проверка с помощью bin: {bin(n)}")
print(f"Проверка с помощью oct: {oct(n)}")
