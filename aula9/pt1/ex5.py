from random import randint
a = [0]*6
f = []
for c in range(6000):
    x = randint(1, 6)
    a[x-1] += 1
for c in range(6):
    f.append(a[c]*100/6000)
    print(f'A face {c + 1} teve a frequência de {f[c]:.2f} o que é {a[c]} vezes')

