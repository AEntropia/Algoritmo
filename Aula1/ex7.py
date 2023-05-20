vd = float(input('Digite o valor do depósito: '))
vt = float(input('Digite o percentual da taxa: '))
print(f'O rendimento será de {vd * (vt/100)}, e o valor total será de {vd + vd * (vt/100)}')
