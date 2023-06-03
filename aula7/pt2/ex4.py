s, c = 0, 0
while True:
    i = int(input('Digite sua idade: '))
    if i == 0:
        break
    s += i
    c += 1
print(f"A média de idade é: {s/c} e a quantidade de idades coletadas foi {c}")
