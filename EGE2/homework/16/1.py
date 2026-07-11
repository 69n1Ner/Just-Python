def f(n):
    if n>30:
        return n**2+5*n+4
    elif n<=30 and n%2==0:
        return f(n+1)+3*f(n+4)
    else:
        return 2*f(n+2)+f(n+5)
k=0
for n in range(1,1000+1):
    F=str(f(n))
    summ = 0
    for i in F:
        summ+=int(i)
    if summ==27:
        k+=1
print(k)
