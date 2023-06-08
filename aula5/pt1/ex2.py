n = []
s, m = 0, 0
for c in range(3):
    n.append(int(input('Digite uma nota: ')))
    s += n[c]
m = s/3
if m < 3:
    print('Reprovado!')
elif m < 7:
    print('Exame!')
else:
    print('Aprovado')
