def reverse_arr():
    x = input()
    if x != '.':
        reverse_arr()
    print(x)
reverse_arr()
