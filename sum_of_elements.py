def count_number_elements(number):
    summ = 0
    number = list(str(number))
    for i in number:
        summ += int(i)
    return summ


print(count_number_elements(1234))
print(count_number_elements((4637)))