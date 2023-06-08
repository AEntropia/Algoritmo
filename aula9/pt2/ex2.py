m, mr, mt = [], [], []
ma = 0
for c in range(2):
    for c1 in range(2):
        n = int(input('Digite um número: '))
        if n > ma:
            ma = n
        mt.append(n)
    m.append(mt)
    mt = []
for c in range(2):
    for c1 in range(2):
        mt.append(m[c][c1]*ma)
    mr.append(mt)
    mt = []
for c in range(2):
    for c1 in range(2):
        print(f'{c+1},{c1+1} = {mr[c][c1]}')
