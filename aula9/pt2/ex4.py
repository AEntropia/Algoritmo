m = [[1.5, 2.3, 4.8, 3.2],
     [5.1, 6.7, 7.9, 9.2],
     [0.7, 8.6, 2.9, 6.4],
     [3.8, 4.2, 5.5, 1.9]]
mt = [[0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]]
for i in range(4):
    for j in range(4):
        mt[i][j] = m[j][i]
print("A matriz transposta é: ")
for c in range(4):
    print("[", end='')
    for c1 in range(4):
        if c1 < 3:
            print(f'{mt[c][c1]}', end=', ')
        else:
            print(f'{mt[c][c1]}', end='')
    print("]")

