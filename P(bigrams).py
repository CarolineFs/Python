
import re
with open ('news.txt', 'r', encoding = 'UTF-8') as f:
    text = f.read()
punct = '[.,!?:;"\'%&$@#()+-=_<>^][{}]'
def preprocessing (text):
    text=text.strip().lower()
    text=re.sub(punct, '', text)
    words=text.split()
    return words
words = preprocessing (text)
print (words[:200])
def create_dic (words):
    d = {}
    for el in words:
        if el in d:
            d[el]+=1
        else:
            d[el] = 1
    return (d)
words_freq = create_dic(words)
bigrams = []
for i in range (len(words)-1):
    bigram = words[i]+' '+words[i+1]
    bigrams.append(bigram)
bigram_freq=create_dic(bigrams)
from math import log
def count_pmi(x,y):
    p_x = words_freq[x]/len(words)
    p_y = words_freq[y]/len(words)
    p_xy = bigram_freq[x + ' ' + y]/len(bigrams)
    pmi = log(p_xy/(p_x*p_y))
    return pmi
pmi_count = {}
for bigram in bigrams:
    x,y = bigram.split(' ')
    try:
        pmi = count_pmi(x,y)
        pmi_count[bigram] = pmi
    except Keyerror:
        continue
i = 0
for key in sorted(pmi_count, key = lambda bigr: -pmi_count[bigr]):
    print(key, pmi_count[key])
    if i > 200:
        break
    i += 2
