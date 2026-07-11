f = [0]*10000
for n in range(0, 10000):
    if n < 11:
        f[n] = n
    else:
        f[n] = n + f[n - 1]
print(f[2024] - f[2021])
