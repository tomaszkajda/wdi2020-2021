# Zadanie 1. Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.


fib1=1
fib2=1
while fib2<10**6:
    print(fib1)
    print(fib2)
    fib1 += fib2
    fib2 += fib1
