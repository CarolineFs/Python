import random
arr = []
for i in range (20):
    arr.append(random.randint(1, 100))
maximum = arr[0]
ind = 0
for i in range (0, 20):
    if arr[i] > maximum:
        maximum = arr [i]
        ind = i
print (arr)
print (maximum, ind)
