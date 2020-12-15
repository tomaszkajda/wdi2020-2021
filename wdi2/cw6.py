
n = int(input('>'))

best = n
for i in range(n//2+1):
    r = 0
    for j in range(n//2+1):
        if i*j == n:
            r = abs(i-j)
            if r < best:
                best = r
                a1, a2 = i, j

print(a1, a2)

