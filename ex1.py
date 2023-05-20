s = 0
for i in range(1,11):
    idade = int(input(f'Digite a {i}° idade: '))
    s += idade
m = s/10
print(f'A média é: {m:.2f}')
