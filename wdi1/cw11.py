#Zadanie 11. Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

def sumofdividers(num):
    sum_div = 0
    for i in range(1, int((num+2)/2)):
        if num % i == 0:
            sum_div += i
    return sum_div

def cw11_2():
    num1 = 1
    num2 = 1
    while num1 <= 10**6:
        sum1 = sumofdividers(num1)
        while num2 <= 10**6:
            sum2 = sumofdividers(num2)
            if sum2 == num1 and sum1 == num2:
                return(num1, num2)
            num2 += 1
        num1 +=1
