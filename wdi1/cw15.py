
 #Zadanie 15. Nieskończony iloczyn sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗
 #sqrt(0.5))) ∗ ... ma wartość 2/π. Napisz program korzystający z tej zależności i wyznaczający wartość π.
from math import sqrt

def cw15():
    eps = 0.0000000001
    value_before = 0
    value_after = sqrt(0.5)
    while value_before >= eps:

        value_before = value_after
        value_after *= sqrt(0.5+0.5*value_after)
    return(2 / value_after)

