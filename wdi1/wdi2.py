#Zadanie 8. Napisać program sprawdzający czy zadana liczba jest pierwsza.
from math import sqrt

def lpierwsza(a):

    if a == 2 or a == 3: return True
    elif a<2 or a % 3 == 0 or a % 2 == 0 : return False
    j = 5
    while j <= sqrt(a):
        if a % j == 0: return False
        j += 2
        if a % j == 0: return False
        j += 4
    return True


lpierwsza(15)