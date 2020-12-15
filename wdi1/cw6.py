#Zadanie 6. Proszę napisać program rozwiązujący równanie x^x = 2020 metodą bisekcji

def f(x):
    return x**x-2020

def cw6():
    eps = 0.00000001
    a = 0 #początek przedziału
    b = 100 #koniec przedziału
    while abs(a-b) >= eps:
        mid = (a + b) / 2
        if mid <= eps:
            break
        if f(a)*f(mid)<0:
            b = mid
        if f(b)*f(mid)<0:
            a = mid
    print(mid)
