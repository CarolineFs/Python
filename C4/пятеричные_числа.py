s = input()
s = s.replace('.', '')
words = s.split()
w = ''
summ = 0
for i in range(len(words)):
    for j in words[i]:
        if (j == '0') or (j == '1')  or (j == '2') or (j == '3') or (j == '4'):
            w += j
        else:
            w = ''
            break
    if w != '':
        n = int(w)
        p = 1
        while n != 0:
            summ += (n%10)*p
            p *= 5
            n = n //10
    w = ''
print (summ)
