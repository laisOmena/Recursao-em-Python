def cont(text):
    if len(text) == 0:
        return 0
    else:
        return len(text.split(x)) - 1

text = "estrutura de dados"
x = input("Digite uma letra: ")
print(cont(text))