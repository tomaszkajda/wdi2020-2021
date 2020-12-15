"""Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Napisać program, który znajdzie wyraz
początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków"""

def cw16():
    steps = 0
    n = 2
    best = 0
    best1 = 0
    best2 = 0
    for n in range(2,10001):
        steps = 0
        best1 = n
        while n != 1:
            n = ((n%2)*(3*n+1))+((1-(n%2))*(n/2))
            steps += 1
        if steps > best:
            best = steps
            best2 = best1
    print(best2, best)
