m = 0
i = 0
v = list(range(1, 11))
for i in v:
    if i > m:
        m = i
        i = v.index(m)
print(f'O maior número é {m} e seu índice é {i}')
