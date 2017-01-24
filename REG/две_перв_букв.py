#Программа ищет слова, начинающиеся на аб, ав, об или ов
import re
with open ('anna.txt', 'r', encoding = 'utf-8') as f:
    text = f.read().replace('\n', '').lower()
    words = text.split()
    for word in words:
        m = re.match('(а|о)(б|в)', word)
        if m != None:
            print (word)
