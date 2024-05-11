# Using sieve of Eratosthenes, it could probably be faster/better programmed but yolo

n = 1000000

prime = [True] * (n+1)
prime[0] = prime[1] = False
p = 2

prime_nums = []

while (p * p <= n):
    if (prime[p] == True):
        for i in range(p * p, n+1, p):
            prime[i] = False
    p += 1

for p in range(2, n+1):
    if prime[p]:
        prime_nums.append(p)

print(prime_nums[10000])