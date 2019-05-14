word = input("Digite uma palavra: ")
def inverso(word):
    if len(word) == 0 or word != word[::-1]:
        return "Não é palíndroma."
    elif word == word[::-1]:
        return "É palíndroma"
print(inverso(word))