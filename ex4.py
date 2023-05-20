a = 0
b = 1
n = int(input(f'Digite um número inteiro: '))
for f in range(1, n):
    print(b)
    a, b = b, a+b
