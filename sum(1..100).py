def one_hundred(n):
    return sum(range(0,101)) ** 2

def one_hundred2(n):
    i = 0
    summa = 0
    result = 0
    while i <= n:
        summa = i
        summa = summa ** 2
        result += summa
        i += 1
    return result

def final_score(n):
    return one_hundred(n) - one_hundred2(n)

print(final_score(100))