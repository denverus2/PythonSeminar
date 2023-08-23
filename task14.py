# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
import math
def allBiPow(n):
  biArr=[]
  i=1
  while pow(2,i)<=n:
    biArr.append(pow(2,i))
    i+=1
  return biArr    
    
  


try:
  n=int (input("Введите число n? "))
  print (allBiPow(n))
except:
  print("Ты чо ввел, бро?")