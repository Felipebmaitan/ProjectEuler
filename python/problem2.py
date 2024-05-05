a = 1
b = 0
sum = 0

while b < 4000000:
    a += b
    b += a
    
    if a % 2 ==0:
        sum += a
    elif b % 2 == 0:
        sum +=b

print(sum)