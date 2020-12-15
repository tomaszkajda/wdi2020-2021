#Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego

# 1 1 2 3 5 8 13 21


inp = int(input('podaj liczbę:'))
a1 = 1
b1 = 1
res = 0
for a in range(1, inp):
    f0 = a1
    f1 = b1
    for b in range(1, inp):
        res = f1 * f0
        f0, f1 = f1, f0 + f1
        if res == inp:
            print('tak')
            exit(0)
print('nie')

