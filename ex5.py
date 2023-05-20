b = int(input('Digite a base: '))
n = int(input('Digite o número final: '))
c = 1
s = 0
while c <= n:
    s += b**c
    c += 1
print(f'A soma é: {s}')
