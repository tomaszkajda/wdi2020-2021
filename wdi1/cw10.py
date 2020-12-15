#Zadanie 10. Napisać program wyszukujący liczby doskonałe mniejsze od miliona.


number = 1
div = 1
while number <= 10**6:
    sum1 = 0
    for div in range(1, int((number+2)/2), +1):
        if number % div == 0:
            sum1 += div
    if sum1 == number:
        print(number)
    number += 1
