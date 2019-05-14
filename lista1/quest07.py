def dia_da_semana(n):
    if n <= 7 and n > 0:
        dia = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sábado"}
        return dia[n]
    else:
        return "Valor inválido"
n = int(input("Digite um número: "))
print(dia_da_semana(n))