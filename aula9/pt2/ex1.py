m = []
mt = []
for c in range(2):
    for c1 in range(2):
        n = int(input('Digite um número: '))
        mt.append(n)
    m.append(mt)
    mt = []
for c in range(2):
    for c1 in range(2):
        print(f'{c+1},{c1+1} = {m[c][c1]}')
