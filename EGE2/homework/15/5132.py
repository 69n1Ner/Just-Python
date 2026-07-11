def od(n,m):
   for d in range(2,max(n,m)+1):
       if n%d==0 and m%d==0:
           return True
   return False
for A in range(1,600):
    fl=True
    for x in range(1,600):
        f=(od(x,42) <= (not(od(x,7)))) or (x+A>=25)
        if not f:
            fl=False
            break
    if fl:
        print(A)
        break