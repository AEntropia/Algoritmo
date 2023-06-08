a = open("texto.txt", encoding="utf-8")
t = a.read()
t1 = t.split('\n')
t2 = []
s = 0
m = []
for i in t1:
    t2.append(i.split(','))
for c in range(len(t2)):
    s += int(t2[c][1])
for c in range(len(t2)):
    m.append(int(t2[c][1])*100/s)
a.close()
a = open('relatorio.txt', 'w', encoding="utf-8")


def escreva(c1):
    return f'{t2[c1][0]:15}{t2[c1][1]+"Kb":20} {m[c1]:.2f}%\n'


a.write(f'{"Nome":15}{"Esp. utilizado":20}{"Porcentagem"}\n' + "-"*47 + "\n")
for c in range(len(t2)):
    a.write(escreva(c))
a.write("-"*47)
a.close()
