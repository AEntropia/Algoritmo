n = 0
while True:
    n = int(input('Digite um número natural: '))
    if n > 0:
        break
print(f'O seu quadrado é {n**2}, seu cubo é {n**3} e sua raiz quadrada é {n**0.5}')
