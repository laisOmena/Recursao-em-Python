def soma(valor):
    if valor == 0:
        return 0
    else:
        return valor + soma(valor - 1)
valor = int(input("Digite um valor: "))
print(f"A soma de 1 até {valor} é {soma(valor)}")