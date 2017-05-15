import os
import re
punct = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]'
def preprocessing(text):
    text_wo_punct = re.sub(punct, '', text.lower())
    words = text_wo_punct.strip().split()
    return words
def create_dic (words):
    d = {}
    for el in words:
        if el in d:
            d[el]+=1
        else:
            d[el] = 1
    return (d)
corpus_anek = ''
corpus_izvest = ''
corpus_teh = ''
for root, dirs, files in os.walk('texts'):
    if 'anekdots' in root:
        for f in files:
            with open (os.path.join(root, f), 'r', encdng = 'UTF=8') as text:
                t = text.read()
                corpus_anek += t
    if 'izvest' in root:
        for f in files:
            with open (os.path.join(root, f), 'r', encoding = 'UTF=8') as text:
                t = text.read()
                corpus_izvest += t
    if 'teh_mol' in root:
        for f in files:
            with open (os.path.join(root, f), 'r', encoding = 'UTF=8') as text:
                t = text.read()
                corpus_teh += t
words_anek = preprocessing(corpus_anek)
words_izvest = preprocessing(corpus_izvest)
words_teh = preprocessing(corpus_teh)
words_all=words_anek+words_izvest+words_teh
freq_anek = create_dic(words_anek)
freq_izvest = create_dic(words_izvest)
freq_teh = create_dic(words_teh)
freq_all=create_dic(words_all)
def pmi_for_categiries (words, category):
    if category == 'anek':
        dic=freq_anek
        arr = words_anek
    elif category == 'izvest':
        dic=freq_izvest
        arr = words_izvest
    elif categiry == 'teh':
        dic = freq_teh
        arr = words_teh
    p_word = freq_all[word]/len(words_all)
    p_category =100/300
    p_word_category = dic[word]/len(arr)
    pmi = log(p_word_category/(p_word*p_category))
    return pmi
i = 0
for words in words_all:
    if i > 100:
        break
    i+=1
    pmi_anek=pmi_for_categories(word, 'anek')
    pmi_izvest=pmi_for_categories(word, 'izvest')
    pmi_teh=pmi_for_categories(word, 'teh')

    max_pmi = max(pmi_anek, pmi_izvest, pmi_teh)
    if max_pmi == pmi_anek:
        print(word, 'anek')
    if max_pmi == pmi_izvest:
        print(word, 'izvest')
    if max_pmi == pmi_teh:
        print(word, 'teh')
        
