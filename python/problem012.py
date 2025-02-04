# At first, I tried doing this using brute force, but the algorithm was taking too long to run
# Then I remembered the idea I used on problem003. That is, if a number "x" is a divisor of
# sqrt(n), then "n/x" is also a divisor. This reduces the algorithm complexity from O(n) to O(sqrt(n)).

a = 1
b = 2

while True:
    a += b
    b += 1
    divisors = set()
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            divisors.add(i)
            divisors.add(a // i)
    if len(divisors) >= 500:
        print(a)
        break