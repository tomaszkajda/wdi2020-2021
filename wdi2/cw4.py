'''Zadanie 4. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
od 1 do N włącznie.'''
end = None

n = int(input('>'))
count = 0

a2 = 1
while a2 <=n:
    a3 = a2
    while a3 <= n:
        a5 = a3
        while a5<=n:
            count += 1
            a5 *= 5
        end
        a3 *= 3
    end
    a2 *= 2
end
print(count)

