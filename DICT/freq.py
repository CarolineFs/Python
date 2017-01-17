with open ('annna.txt', 'r', encoding = 'utf - 8') as anna_file:
    text = anna_file.read()
    text = text.replace ('/n', ' ')
    text = text.lower()
    words = text.split()
    punct = ',()!?;:.<>}{[]|\/'
    words = [word.strip(punct) for word in words
             if word != '' or word != ' ']
    freq = {}
    for word in words:
        try:
            freq[word] += 1
        except:
            freq[word] = 1
    freq2 = sorted (freq)
    for word in freq2:
        print(word, freq[word])
    
