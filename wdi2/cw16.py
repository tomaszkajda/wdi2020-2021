from math import sqrt
def prime( a ):
    if a == 2 or a == 3: return True
    if a < 2 or a % 2 == 0 or a % 3 == 0: return False
    j = 5
    while j <= sqrt(a):
        if a % j == 0:
            return False
        j += 2
        if a % j == 0:
            return False
        j += 4
    return True


def div(n):
    copy, cp1 = n, n
    sum1 = 0
    sum = 0
    i = 2
    while copy > 0:
        sum1 += copy % 10
        copy //= 10
    while n != 0:
        while prime(i) is True:
            if n % i == 0:
                n //= i
                c = i
                while c > 0:
                        sum += c % 10
                        c //= 10
            if n == 1 or n == 0:
                if sum1 == sum:
                    return True
                else:
                    return False
            if i > n//2:
                return False
            i += 1
        i += 1



def cw16(n=10**4):
    for i in range(10, n):
        if div(i) is True:
            print(i)

cw16()
