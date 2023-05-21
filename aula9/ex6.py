from random import randint
a = [0]*11
f = []
for c in range(30000):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    x = d1 + d2
    a[x-2] += 1
for c in range(11):
    f.append(a[c]*100/30000)
    print(f'A soma {c + 2} teve a frequência de {f[c]:.2f} o que é {a[c]} vezes')
if a[5]*100/6000 == 1/6:
    print(f'A soma de sete corresponde exatamente a 1/6 das somas')
elif a[5]*100/6000 > 1/6:
    print(f'A soma de sete teve ocorrência maior a 1/6 das somas')
else:
    print(f'A soma de sete teve ocorrência menor a 1/6 das somas')
