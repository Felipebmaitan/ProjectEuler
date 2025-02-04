# This code represents the general solution to finding prime factors of any giver number, not only the one presented by the problem.

n = 600851475143

while n % 2 == 0:
    print (2)
    n /= 2

for i in range(3, int(n ** 0.5)+1, 2):
    while n % i == 0:
        print (i)
        n /= i

if n > 2:
    print(n)