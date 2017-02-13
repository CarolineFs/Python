rus_lat = {}
with open ('латынь.txt', 'r', encoding = 'utf - 8') as f:
    text = f.read()
    text = text.replace ('\n', ' - ')
    words = text.split(' - ')

for i in range (len(words)):
    if i % 2 != 0:
        rus_lat[words[i]] = words [i-1]
    

print(rus_lat)
