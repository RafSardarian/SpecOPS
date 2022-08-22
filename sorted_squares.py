def sorted_list(lst):
    lst2 = []
    for i in lst:
        i = i ** 2
        lst2.append(i)
    return sorted(lst2)

print(sorted_list([2,5,4,3,6,7]))