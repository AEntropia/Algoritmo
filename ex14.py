idades = {
    'Arna': 30,
    'Predo': 45,
    'Jão': 32,
    'Marcola': 18
}
s = 0
for i in idades.values():
    print(f'A idade que está sendo somada é: {i}')
    s += i
m = s / len(idades)
print(f'A média das idade é {m}')