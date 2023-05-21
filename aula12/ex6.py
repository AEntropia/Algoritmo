def tempo(a, b, c):
    h = a * 3600
    m = b * 60
    s = h + m + c
    return s


st = input('Digite a hora em: HH:MM:SS: ')
sa = st.split(':')
n1, n2, n3 = 0, 0, 0
if len(sa) == 3:
    n1 = int(sa[0])
    n2 = int(sa[1])
    n3 = int(sa[2])
if len(sa) == 2:
    n1 = int(sa[0])
    n2 = int(sa[1])
    n3 = 0
if len(sa) == 1:
    n1 = int(sa[0])
    n2 = 0
    n3 = 0
print(f'Isso tem {tempo(n1, n2, n3)} segundos')

