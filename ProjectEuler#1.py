def multiplies_3_or_5(mrange):
    sum = 0
    number = 0
    while number < mrange:
        if number % 3 == 0 or number % 5 ==0:
            sum += number
        number +=1
    return sum

print(multiplies_3_or_5(10))
print(multiplies_3_or_5(100))
print(multiplies_3_or_5(1000))