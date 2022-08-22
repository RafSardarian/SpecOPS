def str_move(str,n):
    return str[-n:] + str[0:-n]



print(str_move("hello",1))
print(str_move("hello",2))