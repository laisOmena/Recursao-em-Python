def num_perfects(number, i, soma):
    if number == 1:
        return number
    else:
        if number % i == 0:
            soma += i
            return i + num_perfects(number, i - 1, soma)
        else:
            return num_perfects(number, i - 1, soma)

number = 26
i = number
soma = 0
print(num_perfects(number, i, soma))