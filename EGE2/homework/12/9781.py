mx=0
s=''
for n in range(10000,4,-1):
    s='1'+'2'*n
    sm=0
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s=s.replace('12','2',1)
        if '322' in s:
            s=s.replace('322','21',1)
        if '222' in s:
            s=s.replace('222','3',1)
    sm=sum(map(int,s))
    mx=max(mx,sm)
print(mx)