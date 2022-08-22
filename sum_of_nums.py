with open("given_file", "r") as file:
    summ = 0
    for line in file:
        summ += int(line)
    print(summ)