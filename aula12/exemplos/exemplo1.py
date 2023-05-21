def de(n=50, x=0):
    for i in range(x, n):
        print('-', end='')
    print()
    de(30)
    print(f'** Usando funções **')
    de(40)
