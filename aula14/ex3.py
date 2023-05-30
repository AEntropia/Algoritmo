s = 0
m = 1
c = 0
x = "3011392313003"
while c < len(x):
    s += int(x[c])
    m *= int(x[c])
    c += 1
print(f'A soma é: {s}, e a multiplicação é: {m}')
