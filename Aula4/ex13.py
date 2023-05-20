sm = float(input('Qual o valor do salário mínimo? '))
qw = float(input('Quantos quilowatts sua casa consumiu? '))
pqw = sm/8
print(f'O preço de cada quilowatt é {pqw}, svocê ira pagar {pqw * qw}, e com desconto sairá {pqw*(qw - qw*0.15)}')
