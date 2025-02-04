# There is a much simpler way of doing this problem, which is by using math.lcm. 
# I don't believe this solution to be very fun tho, so I'd like to take a more mathematical approach. 
# I'll leave the simpler version of the resolution commented here.

# import math

# lcm = 1
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# for i in numbers:
#     lcm = math.lcm(lcm, i)

# print(lcm)

# Now, let's get to the real math using Euclid's algorithm:

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

lcm = numbers[0]

for i in numbers[1:]:
    for j in range(1,21):
        if lcm % j == 0  and i % j == 0:
            gcd = j
    lcm = (lcm*i)/gcd

print(int(lcm))