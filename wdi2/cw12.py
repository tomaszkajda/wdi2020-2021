

num = 51214
num1 = num

count = 0
while num >= 1:
    count += 1
    num //= 10

for i in range(count):
    r = num1 % 10
    if r == count:
        print('tak')
        break
    else:
        num1 //= 10

