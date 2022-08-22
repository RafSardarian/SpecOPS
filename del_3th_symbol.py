def del_3th(text):
    text = list(text)
    del text[2::3]
    text = "".join(text)

    print(text)


res = "Something is a song by the English rock band the Beatles from their 1969 album Abbey Road"
print(del_3th(res))