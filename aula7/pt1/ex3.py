pm, am, maImc, meImc = 0, 0, 0, 100000
for c in range(20):
    p = float(input("Digite o peso: "))
    a = float(input("Digite a altura: "))
    pm += p
    am += a
    if p / (a**2) > maImc:
        maImc = p / (a**2)
    if p / (a**2) < meImc:
        meImc = p / (a**2)
print(f'O peso médio é {pm/20}, a altura média é {am/20}, o maior IMC {maImc}, e o menor imc {meImc}')
