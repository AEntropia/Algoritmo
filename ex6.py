b = int(input('Insira a base do triângulo: '))
h = int(input('Insira a altura do triângulo: '))
while True:
    if b <= 0:
        b = int(input('Insira a base do triângulo: '))
    elif h <= 0:
        h = int(input('Insira a altura do triângulo: '))
    else:
        break
a = b*h/2
print(f'A área é {a}')
