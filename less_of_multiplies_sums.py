def sum_of_multiplies_sums(number):
    count = 0
    multiplies = 1
    for i in list(str(number)):
        count += int(i)
        multiplies *= int(i)
    return multiplies - count


print(sum_of_multiplies_sums(1234))
print(sum_of_multiplies_sums(4635))