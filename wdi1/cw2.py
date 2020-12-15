# Zadanie 2. Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
# do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

target = 2020
best = target
fib1 = 0
fib2 = 0
for a in range(1, target//2):
    for b in range(1, target//2):
        f0 = a
        f1 = b
        while(f0 + f1 < target+2):
            num = f0 + f1
            if num == target and a+b<best:
                fib1 = a
                fib2 = b
                best = a+b
            f0, f1 = f1, num
print(f"ta pierwsza to {fib1} a ta druga to {fib2}")
