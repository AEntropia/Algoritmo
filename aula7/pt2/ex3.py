m, n = 0, 0
while True:
    s = 0
    while True:
        m = int(input("Digite o maior número: "))
        n = int(input("Digite o menor número: "))
        if m > n:
            break
    for c in range(n, m+1):
        s += c
    print(f'A soma é {s}')
    op = input("Quer continuar (s/n): ")
    if op != "s":
        break
