#Zadanie 3. Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
#sumie.

sum = 20
first1 = 1
first2 = 1
current1 = 1
current2 = 1
result = 1 #suma podciągu
if result != sum:
    while result < sum:
        result += current2 #dodajemy wyraz z prawej strony
        current1, current2 = current2, current1 +current2   #ciąg fib
        while result > sum:
            result -= first1    #odejmujemy wyraz z lewej strony
            first1, first2 = first2, first1 + first2 #ciąg fib
            if first2==current2:
                print('nie istnieje!')
                exit(0)

print('istnieje!')
