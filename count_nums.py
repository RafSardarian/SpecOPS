def count_numbers(lst):
    dic = {}
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic



print(count_numbers([1,2,3,4,5,5,6,1,1,2,7]))