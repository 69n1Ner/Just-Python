def ss(n,c):
    s=''
    while n:
        s=str(n%c)+s
        n//=c
    return s
k=0
for c in range(2,36):
    if ss(39,c)[-1]=='3':
        print(c)
        k+=1
print(k)