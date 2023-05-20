def nt(n):
    for i in range(0, n-2):
        if (i+1) * (i+2) * (i+3) == n:
            return True
    return False


c = int(input('Digite um número: '))
print(nt(c))
