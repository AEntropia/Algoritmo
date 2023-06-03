n = int(input('Digite o número: '))
f = 0
if n < 0:
    while n < 0:
        n = int(input('Digite o número: '))
if n == 0 or n == 1:
    f = 1
if n > 1:
    f = n
    while n > 1:
        f = f * (n-1)
        n = n - 1
print(f'O fatorial é: {f}')
