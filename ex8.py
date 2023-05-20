nv_n = 0
n = input('Digite seu nome: ')
sn = input('Digite seu sobrenome: ')
nf = n + " " + sn
n1 = ''
for i in nf:
    if i != " ":
        n1 += chr(ord(i) + 1)
    else:
        n1 += i
print(n1)

# Primeiro racunho
'''for i in nf:
    if i != " ":
        n1 = chr(ord(i) + 1)
        print(n1, end="")
    else:
        print(i, end="")'''
