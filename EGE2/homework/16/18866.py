f=[0]*20000
for n in range(0,20000):
    if n<100:
        f[n]=n*n
    elif n>99 and n%2==0:
        f[n]=0.5*f[n-1]
    elif n>99 and n%2!=0:
        f[n]=2*f[n-1]
print(1000*(f[16384]/f[7777]))