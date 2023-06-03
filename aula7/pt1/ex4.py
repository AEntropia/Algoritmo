sp, co = 0, 0
while True:
    c = int(input("Digite um número: "))
    if c == 0:
        break
    elif c % 2 == 0:
        sp += c
        co += 1
print(f'A média de todos os números pares é: {sp/co}')
