'''Zadanie 3. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.'''

inp = int(input('>'))
inp1 = inp
a = 0

while inp > 0:
    a += inp % 10
    a *= 10
    inp //= 10
if a/10 == inp1:
    print('tak')
else:
    print('nie')

inp1 = int(input('>'))
inp2 = inp1
a1 = 0

while inp1 !=0:
    a1 += inp % 2
    inp1 //= 2
    a1 *= 10

if a1/10 == inp2:
    print('tak')
else:
    print('nie')