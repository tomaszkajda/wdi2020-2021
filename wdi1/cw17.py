"""Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów
ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu."""
def cw17():
    fib1 = 1
    fib2 = 1
    for i in range(1,20001):
        fib1, fib2 = fib2 , fib1 + fib2
        if i <= 20 or i == 20000:
            print(i, fib2/fib1)
