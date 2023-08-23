# Задача 1 HARD по желанию Напишите программу, которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4
from decimal import Decimal

def decimalCalc(n):
  n1=abs(int(n))
  n2=abs(n)-n1
  calcn1=0
  calcn2=0
  if n1==0:
    calcn1=1
  else:
    while n1>0:
      calcn1+=1
      n1=n1//10
      
  while n2!=int(n2):
    calcn2+=1
    n2*=10
  
  return calcn1+calcn2


try:
  n=Decimal(input("Введите число: "))
  print (f'В числе {n} - {decimalCalc(n)} цифр')
except:
  print ("Числа вводим. Десятичный разделитель точка, а не запятая!")