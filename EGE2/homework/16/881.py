def f(n):
    if n<=15:
        return n*n+11
    elif n>15 and n%2==0:
        return f(n//2)+n**3-5*n
    else:
        return f(n-1)+2*n+3
k=0
for n in range(1,1000+1):
    if str(f(n)).count('6')>=3:
        k+=1
print(k)