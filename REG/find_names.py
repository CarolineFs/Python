import re
with open ('cosm.txt', 'r', encoding = 'utf - 8') as f:
    lines = f.readlines()
    reg = '«.*?»(кит)'
    for line in lines:
        name = re.findall(reg,line)
print(name)
        
