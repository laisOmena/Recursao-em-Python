def naturais(n):
    if n == 0:
        return 0
    else:
        n1 = []
        n1.append(naturais(n-1))
        print(n-1, end=" ")
        n2 = n1[::-1]
        return n

n = int(input("Digite um número: "))
print(naturais(n))