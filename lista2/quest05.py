nome = input("Digite seu nome: ")
nome1 = []
for i in range(0, len(nome)):
    nome1.append(nome[i])
nome1 = nome1[::-1]

nome2 = []
for i in range(0, len(nome1)):
    nome2.append(nome1[i])
    if nome1[i + 1] == " ":
        break

nome2 = nome2[::-1]

nome3 = ""
for i in nome2:
    nome3 = nome3 + i

letra0 = []
for i in range(0, len(nome)):
    if nome[i - 1] == " ":
        letra0.append(nome[i])
        break

letra2 = ""
for i in letra0:
    letra2 = i

letra1 =""
for i in nome[0]:
    letra1 = i

print("{},{}. {}.".format(nome3, letra1, letra2))