a = open("frutas.txt", "a", encoding="utf-8")
while True:
    fruta = input('Digite uma fruta: ')
    if fruta == '':
        break
    a.write(f'{fruta}\n')
a.close()
