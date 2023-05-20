h = input('Digite o horário em horas e minutos (h,m) ')
hh = h.split(',')
print(f'Em minutos será: {int(hh[0])*60 + int(hh[1])}')
