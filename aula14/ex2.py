def cousin(x):
    cp = 0
    for c in range(1, x+1):
        if x % c == 0:
            cp += 1
    if cp == 2:
        return True
    else:
        return False


def primo(y):
    co, n = 0, 0
    r = []
    while co < y:
        n += 1
        if cousin(n):
            r.append(n)
            co += 1
    return r


y = 3 * 2 + 5
s = 0
li = primo(y)
for i in li:
    s += i
print(f'A soma é: {s}')
