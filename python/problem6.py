square_sum = 0
sum_squares = 0

square_sum = (50.5 * 100) ** 2

for i in range(1, 101):
    sum_squares += i ** 2

print(sum_squares - square_sum)