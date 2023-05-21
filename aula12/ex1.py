def par(x):
    if x % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
print(f'O número {n} é {par(n)}, logo é', end=' ')
if par(n):
    print('par')
else:
    print('impar')
