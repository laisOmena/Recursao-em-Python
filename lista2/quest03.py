def ultima_palavra(lista):

    lista2 = []

    for i in range(0, len(lista)):
        lista2.append(lista[i])

    lista2 = lista2[::-1]

    lista3 = []

    for i in range(0, len(lista2)):
        lista3.append(lista2[i])
        if lista2[i+1] == " ":
            break

    lista3 = lista3[::-1]

    lista4 = ""

    for i in lista3:
        lista4 = lista4 + i
    return lista4

lista = input("Digite: ")
print(ultima_palavra(lista))