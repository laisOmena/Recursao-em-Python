def cont(k, n):
  if n == 0:
    return 0
  else:
    return cont(k, n / 10) + (n % 10 == k)

n = float(input("Digite um número: "))
k = int(input("Digite o número que deseja verificar: "))
print(cont(k, n))