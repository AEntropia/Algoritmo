n, co = 0, 0
while n <= 1:
    n = int(input("Digite um número maior que 1: "))
for c in range(n, 0, -1):
    if n % c == 0:
        co += 1
if co == 2:
    print("É primo")
else:
    print("Não é primo")
