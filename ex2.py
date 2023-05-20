e = 0
n = int(input('Digite um número inteiro: '))
for i in range(n):
    e += 2**(i+1)
print(f'O valor é: {e}')
