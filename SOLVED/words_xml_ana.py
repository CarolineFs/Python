#Посчитайте среднее количество разборов (тэг ana) на слово (тэг w).
#Составьте частотный словарь всех частей речи в тексте. Например: {'APRO': 5, 'S': 277, ...}. Распечайте содержимое словаря в отдельный файл (на каждой строке "часть речи"<табуляция>"частотность").
#Найдите в тексте все существительные в творительном падеже (обратите внимание, что некоторые разборы омонимичные. 
#Если хотя бы один разбор с указанием творительного падежа присутствует, слово берём). 
#Запишите в отдельный файл найденные существительные и контекст их употребления в таком формате:
#3 слова слева<табуляция>найденное существительное<табуляция>3 слова справа.


import re
def openfile ():
    with open ('text.xml', 'r', encoding = 'UTF-8') as f:
        text = f.read()
    return text
def aver_ana_per_words ():
    text2 = openfile()
    ana = re.findall(r'<ana', text2)
    ana = len(ana)
    words = re.findall(r'<w>', text2)
    words = len(words)
    av = ana/words
    return av
def all_pos ():
    text3 = openfile()
    pos_dict = {}
    pos = re.findall(r'gr="(\w+)', text3)
    for i in pos:
        if i not in pos_dict:
            pos_dict[i] = 1
        else:
            pos_dict[i] += 1
    
    return pos_dict
def writefile():
    d = all_pos()
    with open ('Parts of speech frequency', 'w', encoding = 'UTF-8') as f:
        for pos in d:
            f.writelines(pos+'\t'+str(d[pos])+'\n')
def instr():
    text4 = openfile()
    nouns = re.findall(r'>(\w+)<ana lex="\w+" gr="S,\w,\w\w\w\w=ins', text4)
    text4 = re.findall(r'>(\w+)<', text4)
    for i in range(len(text4)):
        for j in nouns:
            if j == text4[i]:
                print(j)
                with open ('instr.txt', 'w', encoding = 'UTF-8') as f:
                    f.writelines(text4[i-3]+' '+text4[i-2]+' '+text4[i-i]+'\t'+text4[i]+'\t'+text4[i+1]+' '+text4[i+2]+' '+text4[i+3])
    return nouns



def main():
    print (aver_ana_per_words ())
    writefile()
    instr()
if __name__ == '__main__':
    main()

