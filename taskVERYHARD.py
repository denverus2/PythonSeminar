# Задача VERY HARD необязательная
# Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8


def seekMaxSequence(arr):
    min = arr[0]
    max = arr[0]
    maxSeq = 0
    curSeq = 0

    for n in arr:
        if n < min:
            min = n
        if n > max:
            max = n

    curSeqMin = min
    for i in range(min, max+1):
        curSeq += 1
        if (i in arr and i + 1 in arr):
            if curSeq == 1:
                curSeqMin = i
            curSeq = curSeq + 1
        else:
            if curSeq > 1 and curSeq > maxSeq:
                maxSeq = curSeq
                seqMin = curSeqMin
                seqMax = i
            curSeq = 0

    if maxSeq > 1:
        return seqMin, seqMax
    else:
        return -1


n = [1, 5, 2, 3, 4, 6, 1, 7]
# n= [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ]
# n=[1, 5, 3, 4, 1, 7, 8 , 15 , 1 ]
print(seekMaxSequence(n))
