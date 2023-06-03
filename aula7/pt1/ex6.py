n = int(input("Digite um número: "))
for c in range(n-1, 0, -1):
    n *= c
print(f'O fatorial é: {n}')
