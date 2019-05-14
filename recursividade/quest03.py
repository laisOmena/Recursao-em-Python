def pot(b, p):
  if p == 0:
    return 1
  return b * pot(b, p-1)

b = int(input("Enter a number: "))
p = int(input("Enter a number: "))
print(pot(b, p))