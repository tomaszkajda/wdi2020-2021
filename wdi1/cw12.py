# Zadanie 12. Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.

def nwd(a,b):
    while a % b != 0:
        a, b = b, a % b
    return(b)

def cw12():
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    nwd1 = min(nwd(a, b), nwd(a, c), nwd(b, c))


def cw13():
    #nww = a*b/nwd(a,b)

    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    nww_ab = a*b/nwd(a,b)
    nww_ac = a*c/nwd(a,c)
    nww_bc = b*c/nwd(b,c)

    return(max(nww_ab,nww_ac,nww_bc))