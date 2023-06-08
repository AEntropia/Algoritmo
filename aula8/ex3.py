n = input("Digite um número de nove caracteres: ")
nn = ''
for c in range(len(n)):
    nn += n[c]
    if c == 0:
        nn += '.'
    if c == 3:
        nn += '.'
    if c == 6:
        nn += ','
print(nn)
