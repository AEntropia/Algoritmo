p = input("Digite uma palavra: ").lower()
pa = p[::-1]
if p == pa:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
