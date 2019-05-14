texto = input("Digite seu texto: ")
def cont_palavra(texto):
    if len(texto) == 0:
        return 0
    palavras = verificador(texto)
    for letra in texto:
        if (letra == " "):
            palavras += 1
    return palavras

def verificador(texto):
    palavras = 1
    if texto[0] == " ":
        palavras -= 1
    return palavras

print(cont_palavra(texto))