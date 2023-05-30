n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
op = int(input("Digite a sua opção\n1 - Média\n2 - Diferença\n3 - Produto\n4 - Divisão\n"))
if op == 1:
    print(f'A média é: {(n1+n2)/2}')
elif op == 2:
    if n1 > n2:
        print(f'A diferença é: {n1-n2}')
    else:
        print(f'A diferença é: {n2 - n1}')
elif op == 3:
    print(f'O produto é: {n1*n2}')
elif op == 4:
    if n2 != 0:
        print(f'A divisão é: {n1/n2}')
    else:
        print("Divisão por 0!!!")
else:
    print("Opção inválida")
