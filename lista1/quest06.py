def maior_de_3(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "Não existe maior"
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))
print(maior_de_3(num1, num2, num3))