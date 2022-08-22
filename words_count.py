def count_words(text):
    count = {}
    for i in text.split():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count