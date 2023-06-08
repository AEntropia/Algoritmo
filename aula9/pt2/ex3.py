matriz = [[1.5, 2.3, 4.8, 3.2],
          [5.1, 6.7, 7.9, 9.2],
          [0.7, 8.6, 2.9, 6.4],
          [3.8, 4.2, 5.5, 1.9]]
s = 0
for c in range(4):
    c1 = c
    s += matriz[c][c1]
print(f"A soma da diagonal da matriz é: {s}")
