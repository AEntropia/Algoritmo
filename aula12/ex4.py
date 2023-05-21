a = int(input('Digite um número inteiro para o cálculo de MDC: '))
b = int(input('Digite um número inteiro para o cálculo de MDC: '))


def mdc(n1, n2):
    c2 = 0
    c3 = 0
    c5 = 0
    while True:
        if n1 % 2 == 0 or n2 % 2 == 0:
            if n1 % 2 == 0 and n2 % 2 == 0:
                c2 += 1
            if n1 % 2 == 0:
                n1 = n1/2
            if n2 % 2 == 0:
                n2 = n2 / 2
            pass
        elif n1 % 3 == 0 or n2 % 3 == 0:
            if n1 % 3 == 0 and n2 % 3 == 0:
                c3 += 1
            if n1 % 3 == 0:
                n1 = n1 / 3
            if n2 % 3 == 0:
                n2 = n2 / 3
            pass
        elif n1 % 5 == 0 or n2 % 5 == 0:
            if n1 % 5 == 0 and n2 % 5 == 0:
                c5 += 1
            if n1 % 5 == 0:
                n1 = n1 / 5
            if n2 % 5 == 0:
                n2 = n2 / 5
            pass
        if n1 and n2 == 1:
            break
    return 2**c2 * 3**c3 * 5**c5


print(f'O mdc é {mdc(a, b)}')

