def fibonacci(termo):
    t1 = soma = 0
    t2 = 1
    cont = 3
    while cont <= termo:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        soma = t3 + soma
        cont += 1
    return soma + 1

termo = int(input("Digite um valor: "))
print(fibonacci(termo))