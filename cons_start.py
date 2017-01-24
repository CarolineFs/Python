#Программа ищет слова в файле, в которых есть три согласных подряд 
import re
with open ('anna.txt', 'r', encoding = 'utf-8') as f:
    text = f.read().replace('\n', '').lower()
    words = text.split()
    cons = '[бвгджзйклмнпрстфхцчшщ]'
    for word in words:
        m = re.search(cons + '{5,5}', word)
        if m != None:
            print (word)
