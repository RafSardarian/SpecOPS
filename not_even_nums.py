def not_even(n1,n2):
    lst = []
    for i in range(n1,n2+1):
        if i % 2 == 0:
            continue
        else:
            lst.append(i)
    return lst




print(not_even(3,11))