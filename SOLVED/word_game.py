import random, codecs
with open ('файлПитон.txt', 'r', encoding = 'utf - 8') as f:
    lines = f.readlines()
    random.shuffle(lines)
    score = 0
    for line in lines:
        line = line.strip()
        word, hint = line.split(' ', 1)
        response = input ('Какое слово я загадала?' + 'Подсказка: ' + hint + ' ')
        if response == word:
            print ('Да!')
            score +=1
        else:
            print('Нет, это слово ', word)
with open ('result.txt', 'w', encoding = 'utf - 8') as n:
    n.write('Вот результаты\n')
    n. write (str(score))
