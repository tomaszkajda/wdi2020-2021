

def dasie(n):
    t = [0 for _ in range(n-1)]
    t[0] = 1
    t[1] = 1

    for i in range(2, n-1):
        t[i] = t[i-1] + t[i-2]
    j = 0
    suma = 0
    while suma != n:
        suma = 0
        for k in range(j, n-1):
            suma += t[k]
        j += 1
        if suma == n:
            return True
    return False


n = int(input('>'))
suma = 0
i = 1
while dasie(n+i) is not True:
    i += 1
print(n+1)
