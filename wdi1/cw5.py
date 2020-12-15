#Zadanie 5. Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.


num = 90
eps = 0.00000000001
n = 2   #stopien pierwiastka
a = 1   #początek przedziału
b = 12  #koniec przedziału
while (abs(b-a)>=eps):
    b, a= (1/n)*((n-1)*a+(num/(a**(n-1)))), b
print(a, '\n', b)
