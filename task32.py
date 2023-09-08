# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

def arr_range_index(list_1,mini,maxi):
  return[i for i, x in enumerate(list_1) if mini <= x <= maxi]

list_1=[ 1, 5, 88, 100, 2, -4]
mini = int(input('Введите минимальное значение: '))
maxi = int(input('Введите максимальное значение: '))

print (arr_range_index(list_1,mini,maxi))