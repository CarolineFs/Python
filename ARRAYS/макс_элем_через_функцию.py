import random
def random_search():
    for i in range (20):
        random_number = random.randint(1, 100)
        random_arr.append(random_number)
    max_elem = random_arr[0]
    for elem in range(len(random_arr)):
        if random_arr[elem] > max_elem:
            max_elem = random_arr[elem]
    for elem in range (len(random_arr)):
        if random_arr[elem] == max_elem:
            print(elem)
    print (max_elem)
random_arr = []
random_search()
