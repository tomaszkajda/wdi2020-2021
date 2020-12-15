

def f(x):
    return 1/x
def prostokaty(n, k):
    pole = 0
    liczba = (k-1)/n
    center = (1+liczba)/2
    for i in range(0, 10):
        pole += f(center)*(1+i*liczba)
    return pole

print(prostokaty(2134, 10))