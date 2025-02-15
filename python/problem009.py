#Good ol' bruteforce. Idk if there's another of solving this.

for i in range(0,1000):
    for j in range(0,1000):
        for k in range(0,1000):
            if k<j<i and k**2 + j**2 == i**2 and k+j+i == 1000:
                print(k*j*i)