a = int(input('Digite o ano do seu nascimento: '))
i = 2023 - a
print(f'Você tem {i} anos')
if i > 16:
    print('Você pode votar! ', end='')
if i > 18:
    print('E tirar a carteira de motorista!')

