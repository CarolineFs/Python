word = input ('Введите слово, которое нужно зашифровать: ')
key = input ('Введите ключ: ')
vocab = 'abcdefghigklmnopqrstuvwxyz'
table = []
for i in range (len(vocab)):
    table.append(vocab[:i] + vocab [i:])
if len (key) < len (word):
    whole = len (word)//len(key)
    longkey = key * whole
    longkey +=key[:(len(word) - len (longkey))]
elif len (key) > len (word):
    longkey = key [:len(word)]
cipher = ''
for i in range (len(word)):
    row = vocab.index(longkey[i])
    col = vocab.index(word[i])
    print(longkey[i], word [i], row, col)
    cipher += table [row] [col]
print (cipher)
