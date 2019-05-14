def eh_data_valida(dia, mes, ano):
    value = "true"
    i = 0
    while value == "true" and i == 0:
        if(ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            bissexto = "sim"
        else:
            bissexto = "nao"
        if ano < 1:
            value = "false"
        if 1 > mes > 12:
            value = "false"
        if (dia > 31 or (mes == 4 or mes == 6 or mes == 9 or mes == 11))and dia > 30:
            value = "false"
        if (mes == 2 and bissexto == "nao" and dia > 28) or (mes == 2 and bissexto == "sim" and dia > 29):
            value = "false"
        i += 1
    if value == "true":
        return "True"
    else:
        return "False"

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
print(eh_data_valida(dia, mes, ano))
