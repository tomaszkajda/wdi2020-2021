
"""Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! +
1/2! + 1/3! + ...
"""

eps = 0.0000001
e = 1
silnia = 1
for i in range(1,1000):
    silnia *= i
    e += 1/silnia
print(e)
