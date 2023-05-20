idades = {
    'Arna': 30,
    'Predo': 45,
    'Jão': 32,
    'Marcola': 18
}
ma = 0
nma = ''
for n in idades.keys():
    if len(n) > ma:
        ma = len(n)
        nma = n
print(idades.get(nma))
