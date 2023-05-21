from funcoes import d
from time import sleep
print('-' * 60)
print(f'Fala meu bom, joga o dado aê')
print('-' * 60)
sleep(2)
r = ''
c, u = 0, 0
while r != 'n':
    c = d()
    u = d()
    input('Tecle enter para jogar o dado: ')
    print(f'Você jogou: ', end='')
    print(u)
    print(f'O computador jogou: ')
    for i in range(0, 20):
        sleep(0.1)
        print('.', end='')
    print(c)
    sleep(2)
    if c > u:
        print('-' * 60)
        print('Perdeu!')
        print('-' * 60)
    elif c < u:
        print('-' * 60)
        print('Brabo dms!')
        print('-' * 60)
    else:
        print('-' * 60)
        print('A vitória são os amigos que fazemos no caminho!')
        print('-' * 60)
    r = input('Quer continuar? (y/n): ')
