p = []
n = 100
c = 0
while c < 10:
    n += 1
    c1 = 0
    for i in range(1, n+1):
        if n % i == 0:
            c1 += 1
    if c1 == 2:
        c += 1
        p.append(n)
print(f'Os dez primeiros números primos após o 100 são: {p}')
