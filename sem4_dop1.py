# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.

# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

import random


def multi_dick(k: int) -> str:
    coof = [random.randint(-10, 10) for _ in range(k + 1)]
    formul = ""
    for i, coefficient in enumerate(coof[::-1]):
        if coefficient == 0:
            continue
        degree = k - i
        if degree == 0:
            formul += f"{coefficient}"
        elif degree == 1:
            if coefficient > 0:
                formul += f" + {coefficient}*x"
            else:
                formul += f" - {abs(coefficient)}*x"
        else:
            if coefficient > 0:
                formul += f" + {coefficient}*x^{degree}"
            else:
                formul += f" - {abs(coefficient)}*x^{degree}"
    if formul.startswith(" + "):
        formul = formul[3:]
    return formul + " = 0"


# Пример использования функции
k = 3
polynomial = multi_dick(k)
print(polynomial)
