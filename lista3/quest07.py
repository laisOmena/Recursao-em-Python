def fatorial_duplo(n):
    if n == 1 or n == 0:
        return 1
    else:
        if n % 2 != 0:
            return n * fatorial_duplo(n - 1)
    return fatorial_duplo(n - 1)
n = int(input("Digite um número ímpar: "))
print(fatorial_duplo(n))