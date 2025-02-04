# This uses the Sieve of Eratosthenes to compute all the prime numbers up to a threshold. I used this for my first programming
# class. The professor offered a certain bonus for whoever solved all primes up to a very big number in a certain time,
# and this was the solution I gave him.

n = 2000000

prime = [True] * ((n // 2) +1)
prime[0] = False

sum = 2 # This has to be manually set because 2 is the only even prime. The program only looks for odd numbers.
p = 3

while p * p <= n:
    if prime[p // 2]:
        for i in range(p * p, n+1, 2 * p):
            prime[i // 2] = False
    p += 2

for p in range(3, n+1, 2):
    if prime[p // 2]:
        sum += p

print(sum)