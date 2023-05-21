ma = 0
d = {
    "Silva": 31,
    "Santos": 21,
    "Rosa": 20,
    "Alves": 30,
    "AAlfredo": 80,
    "Antunes": 28,
    "Oliveira": 35,
    "Ferreira": 56,
    "Pinto": 18,
    "Marvollo Riddle": 100
}
for c in d.values():
    if c > ma:
        ma = c
for c in d.keys():
    if d[c] == ma:
        print(c)
