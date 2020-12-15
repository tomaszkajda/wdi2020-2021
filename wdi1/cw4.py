#Zadanie 4. Proszę napisać program obliczający pierwiastek całkowitoliczbowy z liczby naturalnej korzystając z zależności 1 + 3 + 5 + ... = n^2


num = 121
sum = 1
n = 1
while sum <= num:
    sum += 2*n+1
    n+=1
print(n-1)
