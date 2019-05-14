def MDC(a, b):
    if b == 0:
        return a

    r = a % b
    a = b
    b = r
    return MDC(a, b)

a = int(input("Digite: "))
b = int(input("Digite: "))
print(MDC(a, b))