x=int(input('Введите год: '))
if x%4==0 and x%100!=0:
    print ('год високосный') 
elif x%400==0:
    print ('год високосный')
else:
    print ('год не високосый')
