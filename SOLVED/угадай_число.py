a=int (input ('Угадайте число от 1 до 10: '))
if a==int(6):
    print ('Поздравляю, вы угадали')
else:
    if a<6:
        print ('Число больше этого')
    if a>6:
        print ('Число меньше этого')
    b=int(input('Посдледняя попытка: '))
    if b==int(6):
        print ('Да')
    else:
        print ('Нет')
