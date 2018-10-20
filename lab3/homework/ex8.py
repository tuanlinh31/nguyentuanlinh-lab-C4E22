def get_even_list(l=[]):
    new_list = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            new_list.append(l[i])
    return new_list