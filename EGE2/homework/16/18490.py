from filecmp import clear_cache
f=[2]*3010
for n in range(3000,1,-1):
    if n>3000:
        f[n]=n
    else:
        f[n]=(2*n+4)*f[n+2]
print(f[20]/f[28])
