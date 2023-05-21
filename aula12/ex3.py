def bi(i):
    c = 0
    if i % 4 == 0:
        c = 1
        if i % 100 == 0:
            c = 0
            if i % 400 == 0:
                c = 1
    return c


a = int(input('Digite um ano: '))
print(f'O ano é ', end='')
if bi(a):
    print('bissexto')
else:
    print(f'não-bissexto')
