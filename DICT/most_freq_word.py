#Программа должна прочитать текст, создать частотный список слов в этом тексте, 
#используя слова в качестве ключей словаря, а частотность в качестве значений. 
#После этого нужно распечатать самое частотное слово в тексте. 
# Найти среднее значение частотности слов в тексте.
with open ('anna.txt', 'r', encoding = 'utf - 8') as anna_file:
    text = anna_file.read()
    text = text.replace ('/n', ' ')
    text = text.lower()
    words = text.split()
    punct = ',()!?;:.<>}{[]|\/'
    words = [word.strip(punct) for word in words
             if word != '' or word != ' ']
summa = 0
k = 0
freq = {}
for word in words:
    try:
        freq[word] += 1
    except:
        freq[word] = 1
maximum = 0
keys = list(freq.keys())
values = list(freq.values())
for i in values:
    if i > maximum:
        maximum = i;
    summa += i
    k+=1
for key in keys:
    if freq[key] == maximum:
        
        print(key)
print (maximum)
aver_freq = summa%k
print(aver_freq)

