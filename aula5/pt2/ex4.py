l1 = float(input("Digite um lado do triângulo: "))
l2 = float(input("Digite um lado do triângulo: "))
l3 = float(input("Digite um lado do triângulo: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    if l1 == l2 == l3:
        print("Triângulo EQUILÁTERO")
    elif l1 != l2 != l3:
        print("Triângulo ESCALENO")
    else:
        print("Triângulo ISÓSCELES")
else:
    print("Não é um triângulo")
