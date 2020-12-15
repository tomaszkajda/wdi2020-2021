"""Zadanie 1. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego."""

inp = int(input('>'))
fib1 = 1
fib2 = 1
for i in range(inp):
    fib1_z = 1
    fib2_z = 1
    for j in range(inp):
        if (fib1 * fib2_z == inp):
            print('tak')
            exit(0)
        fib1_z, fib2_z = fib2_z, fib1_z+fib2_z
    fib1, fib2 = fib2, fib1 + fib2

print('nie')