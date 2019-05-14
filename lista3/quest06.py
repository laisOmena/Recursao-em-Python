def fibonacci(termo):
    if termo <= 1:
        return termo
    else:
        return fibonacci(termo - 1) + fibonacci(termo -2)

termo = 10
print(fibonacci(termo))