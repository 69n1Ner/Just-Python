def sys_num(n,r):
    s=''
    while n:
        s=str(n%r)+s
        n//=r
    return s
k=0
for r in range(2,30):
    if sys_num(29,r)[-1]=='5':
        k+=1
        print(r)
print(k)