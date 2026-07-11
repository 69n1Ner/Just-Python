def dels(n):
    s=set()
    s.add(n)
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            s|={d,n//d}
    return sorted(s)

for n in range(1000,4,-1):
    s='3'+'7'*n
    while '37' in s or '577' in s or '777' in s:
        if '37' in s:
            s=s.replace('37','7',1)
        if '577' in s:
            s=s.replace('577','73',1)
        if '777' in s:
            s=s.replace('777','5',1)
    sum_s=sum(map(int,s))
    if len(str(sum_s))==2 and len(str(n))==2:
        fl=True
        masn=dels(n)
        mas_s=dels(sum_s)
        for i in masn:
            for j in mas_s:
                if i==j:
                    fl=False
                    break
        if fl:
            print(n)
