number = 2**1000
number_str = str(number)
result = 0

for digit in number_str:
    result += int(digit)

print(result)