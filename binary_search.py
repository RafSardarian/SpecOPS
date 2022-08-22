def binary_search(lst,target):
    begin, end = 0 , len(lst) -1
    while begin <= end:
        middle = begin + (end - begin) // 2
        middle_value = lst[middle]
        if middle_value == target:
            return middle
        elif target < middle_value:
            end = middle - 1
        else:
            begin = middle + 1
    return None


print(binary_search([1,2,3,4,5,6,7,8,9,10],4))
print(binary_search([10,14,15,20,24,25,60,34,35,40,44,45],14))