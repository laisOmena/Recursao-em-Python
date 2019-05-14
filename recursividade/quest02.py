def division(m, n, cont):
  if m == 0:
    return cont
  else:
    if m >= n:
      cont += 1
      return division(m - n, n, cont)
    print(cont)
  return division(m, n, cont)

m = int(input("Enter a number: "))
n = int(input("Enter a number: "))
cont = 0
print(division(m, n, cont))
