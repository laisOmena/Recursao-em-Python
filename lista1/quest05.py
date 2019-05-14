def maior_de_2(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Não existe maior"
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print(maior_de_2(num1, num2))