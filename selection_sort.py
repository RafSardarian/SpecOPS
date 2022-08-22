def selection_sort(lst):
    index = range(0,len(lst)-1)
    for i in index:
        min_value = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_value]:
                min_value = j
        if min_value != i:
            lst[min_value],lst[i] = lst[i],lst[min_value]
    return lst


test = [3,1,2,4]
test2 = [5,2,9,1,6,41,15,32,1]
test3 = [1,1,1,1,2,1,1,1,1,1,1]

print(selection_sort(test))
print(selection_sort(test2))
print(selection_sort(test3))