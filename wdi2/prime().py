from math import sqrt
def prime():
    t = [2,3,5,7]
    i=8
    while i <= 10**6:
        while i % 2 == 0 or i % 3 == 0:
            i += 1
        j = 5
        while j <= sqrt(i):
            if i % j == 0:
                break
            j += 2
            if i % j == 0:
                break
            j += 4
            if j > sqrt(i):
                t.append(i)
        i+=1
        if i == 10**6:
            print('juz')
    return t