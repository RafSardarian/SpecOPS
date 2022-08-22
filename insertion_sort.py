def insertion_sort(lst):
    index = range(1,len(lst))
    for i in index:
        value = lst[i]
        while lst[i-1] > value and i>0:
            lst[i],lst[i-1] = lst[i-1],lst[i]
            i-=1
    return lst


test = [3,1,2,4]
test2 = [5,2,9,1,6,41,15,32,1]
test3 = [1,1,1,1,2,1,1,1,1,1,1]

print(insertion_sort(test))
print(insertion_sort(test2))
print(insertion_sort(test3))