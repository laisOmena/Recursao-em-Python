def compare(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1
a = float(input("Digite um valor: "))
b = float(input("Digite um valor: "))
print(compare(a,b))