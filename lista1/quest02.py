def eh_par(num):
    if num % 2 == 0:
        return "Verdadeiro"
    else:
        return "Falso"
num = int(input("Digite um número: "))
print(eh_par(num))