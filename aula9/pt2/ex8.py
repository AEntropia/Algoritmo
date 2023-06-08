matriz = [[1.5, 2.3, 4.8, 3.2, 0.7],
          [5.1, 6.7, 7.9, 9.2, 3.8],
          [4.2, 5.5, 1.9, 8.6, 2.9],
          [6.4, 3.3, 2.1, 7.2, 4.5],
          [2.6, 1.1, 5.9, 9.8, 0.3]]
s = 0
m = []
for i in range(1, 6):
    for j in range(5):
        if i % 2 == 0:
            s += matriz[i-1][j]
            if j == 4:
                m.append(s/5)
print(f'A média dos números na linha 2 é: {m[0]:.2f} e na linha 4: {m[1]:.2f}')
