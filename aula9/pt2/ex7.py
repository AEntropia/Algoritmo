matriz = [[1, 2, 3, 4, 5, 6, 7, 8],
          [2, 9, 10, 11, 12, 13, 14, 15],
          [3, 10, 16, 17, 18, 19, 20, 21],
          [4, 11, 17, 22, 23, 24, 25, 26],
          [5, 12, 18, 23, 27, 28, 29, 30],
          [6, 13, 19, 24, 28, 31, 32, 33],
          [7, 14, 20, 25, 29, 32, 34, 35],
          [8, 15, 21, 26, 30, 33, 35, 36]]
r = []
for i in range(8):
    for j in range(8):
        if matriz[i][j] == matriz[j][i]:
            r.append(True)
        else:
            r.append(False)
if False in r:
    print("Não é simétrica! ")
else:
    print("É simétrica")
