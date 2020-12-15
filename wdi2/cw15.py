
n = int(input('>'))
for i in range(10**(n-1), 10**n-1):
    suma = 0
    j = i
    while j >= 1:
        suma += (j % 10)**n
        j //= 10
    if suma == i:
        print(i)
