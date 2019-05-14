def fat(valor):
    if valor == 0:
        return 1
    else:
        return valor * fat(valor - 1)
valor = int(input("Digite um valor: "))
print(f"O fatorial de {valor} é {fat(valor)}.")