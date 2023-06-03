m, s1, s2 = 10, 0, 0
while True:
    print(f'{m}:{s1}{s2}')
    if m == 0 and s1 == 0 and s2 == 0:
        break
    elif s1 == 0 and s2 == 0:
        m -= 1
        s1 = 5
        s2 = 9
    elif s2 == 0:
        s1 -= 1
        s2 = 9
    else:
        s2 -= 1
