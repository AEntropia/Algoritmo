i = int(input("Digite a sua idade: "))
if 5 <= i <= 7:
    print("Você está na categoria INFANTIL")
elif i <= 10:
    print("Você está na categoria JUVENIL")
elif i <= 15:
    print("Você está na categoria ADOLESCENTE")
elif i <= 30:
    print("Você está na categoria ADULTO")
else:
    print("Você está na categoria SENIOR")
