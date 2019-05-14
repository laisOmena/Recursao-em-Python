def para_maiusculo(letra):
    if letra in "abcdefghijklkmnoqrstuvwxyz":
        return chr(ord(letra)-32)
    return letra

def converte_title(title):
    result = ""
    for letra in title:
        if letra != " ":
            nova_letra = para_maiusculo(letra)
        else:
            nova_letra = " "
        result += nova_letra + " "
    return result

title = input("Digite: ")
title = converte_title(title)
print(title)
