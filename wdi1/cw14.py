"""
Zadanie 14. Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.
 cos(x) = 1 -sin(x) = 0 -cos(0)=-1 sin(0)=0 cos(0) = 1
 cos(x) = 1 -0 + -1/2! + 0 + 1/4! -0 + -1/6! - 1/8!
"""


def cw14(x):
    cos = 1
    sil = 2
    sil1 = 24
    for n in  range(2, 10**2, +4):
        cos -= (1/sil)*x**n
        sil *=(n+1)*(n+2)*(n+3)*n

    for i in range(4,10**2, +4):
        cos += (1/sil1)*x**i
        sil1 *=(i+1)*(i+2)*(i+3)*i
    print(f'cos({x})= {cos}')

