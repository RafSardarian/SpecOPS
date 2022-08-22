def bubble_sort(lst):
    index = len(lst) -1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,index):
            if lst[i] > lst[i+1]:
                sorted = False
                lst[i],lst[i+1] = lst[i+1],lst[i]
    return lst




test = [3,1,2,4]
test2 = [5,2,9,1,6,41,15,32,1]
test3 = [1,1,1,1,2,1,1,1,1,1,1]

print(bubble_sort(test))
print(bubble_sort(test2))
print(bubble_sort(test3))