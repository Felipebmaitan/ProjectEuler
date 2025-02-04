biggest_chain_size = 0
longest_n = 0

for i in range(2, 1000001):
    n = i
    chain_size = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        chain_size += 1
    if chain_size > biggest_chain_size:
        biggest_chain_size = chain_size
        longest_n = i

print(longest_n)