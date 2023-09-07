# Задача №33. Общее обсуждение
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


def change_qual(mini,maxi,n):
  if n<0:
    return
  else:
    if list1[n]==maxi:
      list1[n]=mini
    change_qual(min,max,n-1)
  
list1=[1, 3, 3, 3, 4]
change_qual(min(list1), max(list1), len(list1)-1)
print(list1)
