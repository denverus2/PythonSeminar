# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
import random

def coin_drop(n):
  coins=[]
  for i in range(n):
    coins.append(random.randint(0,1))
  return coins
def seek_min_rotate(coins):
  avers=0
  revers=0
  for coin in coins:
    if coin==0:
      avers+=1
    else:
      revers+=1
  if avers<revers:
    return avers
  else:
    return revers


try:
  n=int (input("Сколько монеток кидаем? "))
  coins=coin_drop(n)
  print(coins)
  print (f'Минимальное количество переворотов {seek_min_rotate(coins)}')
except:
  print("Ты чо ввел, бро?")