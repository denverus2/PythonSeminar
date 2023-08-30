# sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]
# ответ будет 11 раз

sp = [55.1245, 44 ,"5ррууу55",   [95.45,0.5] , {53:  125} ]

stroku=""
for k in sp:
  stroku=stroku+str(k)
  
n="5"
count=0
summ=0
for i in range(len(stroku)):
  if(stroku[i])==n:
    count+=1
  
print (stroku)    
print (count)