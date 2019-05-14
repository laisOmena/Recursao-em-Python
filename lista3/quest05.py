def naturais(n):
    if n == 0:
        return 0
    else:
        print(n, end=" ")
        return naturais(n-1)

n = int(input("Digite um número: "))
print(naturais(n))