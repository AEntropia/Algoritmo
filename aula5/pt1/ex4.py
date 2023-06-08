a = float(input('Digite a sua altura: '))
s = input('Digite o seu sexo (m/f): ').lower()
pi = 'Não encontrado'
if s[0] == 'm':
    pi = (72.7 * a)-58
elif s[0] == 'f':
    pi = (62.1 * a) - 44.7
else:
    print('Sexo não encotrado!')
print(f'Seu peso ideal é: {pi}')
