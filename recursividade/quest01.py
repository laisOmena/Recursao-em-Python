def soma(n):
  if n == 0 or n == 1:
    return n
  else:
    return n + soma(n - 1)

n = int(input("Enter a number: "))
print(soma(n))