lista = input("Digite seu nome: ")
lista2 = []

for i in range(0, len(lista)):
    lista2.append(lista[i])
print(lista2)
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

lista5 = []
for i in range(0, len(lista)):
    lista5.append(lista[i])
    if lista[i + 1] == " ":
        break

lista6 = ""
for i in lista5:
    lista6 = lista6 + i

print("{}/{}".format(lista4, lista6))