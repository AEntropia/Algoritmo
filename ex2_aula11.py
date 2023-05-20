def cousin(x):
    j = 0
    for c in range(1, x+1):
        if x % c == 0:
            j += 1
    return j > 2


i, c = 0, 1
while i <= 50:
    if not cousin(c):
        i += 1
        if i <= 49:
            print(c, end=' - ')
        else:
            print(c)
    c += 1
