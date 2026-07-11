f=[1]*401000
for n in range(0,400000):
    if n<3000:
        f[n]=n
    if n>=3000 and n%7==0:
        f[n]=n+f[n//7]
    if n>=3000 and n%7!=0:
        f[n]=29+f[n-3]
    if f[n]>100_000:
        print(n)
        break
