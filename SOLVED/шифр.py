# статья про шифр -- https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D0%B8%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B0
# 1. Создать таблицу
# 2. Спросить слово и ключ
# 3. Преобразовать ключ до нужной длины
# 4. Посимвольно кодирую
# таблица выглядит так [[], [], [], [], ...]

alphabet = list('abcdefghijklmnopqrstuvwxyz')
table = []

# создаем таблицу со сдвигами в алфавите
for i in range(len(alphabet)):
    table.append(alphabet[i:] + alphabet[:i])

word = input('Введите слово (английскими буквами): ')
key = input('Введите ключ (английскими буквами): ')

# если ключ длиннее слова, откусываем от него кусок. Если равен по длине, с ним ничего не случится
if len(key) >= len(word):
    key = key[:len(word)]
# если ключ короче слова, удлиняем его
else:
    key *= len(word)//len(key)
    tail = len(word)%len(key)
    key += key[:tail]

cipher = ''

# перебираем попарно буквы в ключе и слове, ищем соответствующую шифровку в таблице
for i in range(len(key)):
    id_row = alphabet.index(key[i]) # индекс нужной строки
    id_col = alphabet.index(word[i]) # индекс нужной колонки
    cipher += table[id_row][id_col] # нужный символ

print('Зашифрованное слово', cipher, end='\n'*2)

# Теперь расшифровываем
cipher = input('Введите зашифрованное слово (английскими буквами): ')
key = input('Введите ключ (английскими буквами): ')

if len(key) >= len(cipher):
    key = key[:len(cipher)]
else:
    key *= len(cipher)//len(key)
    tail = len(cipher)%len(key)
    key += key[:tail]

result = ''
for i in range(len(key)):
    id_row = alphabet.index(key[i]) # индекс нужной строки
    row = table[id_row] # нужная строка
    id_col = row.index(cipher[i]) # нашли индекс нужного символа
    result += alphabet[id_col] # достали его из алфавита

print('Расшифрованное слово', result)
