
def cw13(n):
    last = n % 10
    n //= 10
    while n > 0:
        if last == n % 10:
            return False
        else:
            n //= 10
    return True

print(cw13(52345))
