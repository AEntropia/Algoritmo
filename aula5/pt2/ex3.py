n = float(input("Preço líquido: "))
o = int(input("Código de origem: "))
if o == 1:
    pf = n + (n * 0.11)
    print(f'A procedência é SUL, o preço final é: {pf}')
elif o == 2:
    pf = n + (n * 0.13)
    print(f'A procedência é NORTE, o preço final é: {pf}')
elif o == 3:
    pf = n + (n * 0.09)
    print(f'A procedência é NORDESTE, o preço final é: {pf}')
elif o == 4:
    pf = n + (n * 0.12)
    print(f'A procedência é CENTRO-OESTE, o preço final é: {pf}')
elif o == 5:
    pf = n + (n * 0.18)
    print(f'A procedência é SUDESTE, o preço final é: {pf}')
else:
    print("Código errado!")
