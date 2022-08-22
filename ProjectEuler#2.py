def fib_seq(n,a=0,b=1):
    return a if n == 1 else fib_seq(n-1,b,a+b)

def sum_of_even(num):
    sum = 0
    even = 1
    while fib_seq(even) < num:
        if fib_seq(even) % 2 == 0:
            sum += fib_seq(even)
        even+=1
    return sum

print(sum_of_even(50))
print(sum_of_even(600))
print(sum_of_even(1000))
print(sum_of_even(4000000))