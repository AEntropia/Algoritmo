def fib(i):
    """ Retorna fibonacci """
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i - 1) + fib(i-2)


'''for c in range(0, 11):
    print(fib(c), end=' ')'''
