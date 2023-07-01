def sequencia_fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sequencia_fibonacci(n-1) + sequencia_fibonacci(n-2)