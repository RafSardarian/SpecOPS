with open("Lorem_Ipsum", "r") as file:
    test = file.read()


def count_symbols(text):
    summ = 0
    for i in text:
        if i == " ":
            continue
        summ += 1
    print(summ)


print(count_symbols(test))