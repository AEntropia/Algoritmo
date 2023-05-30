a = open("frutas.txt", encoding="utf-8")
t = a.read()
t1 = t.split("\n")
t1.pop(len(t1)-1)
a.close()
a = open("frutas.txt", "a", encoding="utf-8")
while True:
    fruta = input("Digite uma fruta: ")
    if fruta == '':
        break
    elif fruta in t1:
        print(f'Fruta repetida parcero')
    else:
        a.write(f'{fruta}\n')
a.close()
