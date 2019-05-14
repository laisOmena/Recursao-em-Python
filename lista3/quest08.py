'''def palindroma(text):
    word = text.split(" ")
    new_text = ''.join(word)
    inverso = new_text[::-1]
    if inverso == 0 or inverso != new_text:
        return "Não é palíndroma"
    else:
        if inverso == new_text:
            return "É palíndroma"

text = input("Digite: ")
print(palindroma(text))
