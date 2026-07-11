f=[0]*1000
for n in range(1,100+1):
    if n<=3:
        f[n]=n
    if n>3 and n%3==0:
        f[n]=n**3+f[n-1]
    if n>3 and n%3==1:
        f[n]=4+f[n//3]
    if n>3 and n%3==2:
        f[n]=n**2+f[n-2]
print(f[100])
