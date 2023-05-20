s = 0
dic = {}
for c in range(5):
    n = input("Digita o nome: ")
    dic[n] = int(input("Digite a idade: "))
for c in dic.values():
    s += c
m = s / len(dic)
for c in dic.values():
    if c > m:
        print(c)
