import os
text = 'Hello'
i = 1
for f in os.listdir('.'):
    if f.endswith('.txt'):
        with open (f, 'a', encoding = 'utf - 8')as w:
            w.write(text*i)
            i += 1
