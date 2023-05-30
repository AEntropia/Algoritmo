a = open("texto.txt", encoding="utf-8")
t = a.read()
t1 = t.split('\n')
t2 = []
s = 0
m = []
print(f'{"Nome":15}{"Esp. utilizado":20}{"Porcentagem"}')
print("-"*47)
for i in t1:
    t2.append(i.split(','))
for c in range(len(t2)):
    s += int(t2[c][1])
for c in range(len(t2)):
    m.append(int(t2[c][1])*100/s)
    print(f'{t2[c][0]:15}{t2[c][1]+"Kb":20} {m[c]:.2f}%')
a.close()
