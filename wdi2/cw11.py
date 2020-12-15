
n = int(input('>'))

def cw11(n):
    n1 = n
    count = 0
    r = 0
    # z prawej w lewa
    while n1 >= 1:
        r1 = n1 % 10
        if r1 < r:
            r = r1
            n1 //= 10
        else:
            count += 1
    r = 0
    # z lewej w prawa
    while n>=1:
        r1 = n % 10
        if r1 > r:
            r = r1
            n //= 10
        else:
            count +=1
    if count == 2:
        return False
    else:
        return True

print(cw11(n))

