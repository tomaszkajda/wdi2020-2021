"""Zmodyfikować wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3."""

def cw18(num):
    eps = 0.00000000001
    n = 3   #stopien pierwiastka
    a = 1   #początek przedziału
    b = 12  #koniec przedziału
    while (abs(b-a)>=eps):
        b, a= (1/n)*((n-1)*a+(num/(a**(n-1)))), b
    print(a, '\n', b)
