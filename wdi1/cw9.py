
#Zadanie 9. Napisać program wypisujący podzielniki liczby.


num = int(input('podaj liczbę: '))
for i in range(1, num+1):
    if num % i == 0:
        print(i)
