def inverte(word):
    if len(word) == 0:
        return 0
    else:
        word = word[0][::-1]
        return word

word = ["Python"]
print(inverte(word))