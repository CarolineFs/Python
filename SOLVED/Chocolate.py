x=int(input('Введите длину шоколадки: '))
y=int(input('Введите ширину шоколадки: '))
z=int(input('Введите количество клеточек: '))
if (z%x==0 and x*y>=z) or (z%y==0 and x*y>=z):
    print('да')
else:
    print ('нет')
    
