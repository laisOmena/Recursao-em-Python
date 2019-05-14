def eh_primo(num):
    tot = 0
    for i in range(1, num + 1):
        if num % i == 0:
            tot += 1

    if tot == 2 and num > 1:
        return True
    else:
        return False

num = int(input("Digite um número: "))
print(eh_primo(num))