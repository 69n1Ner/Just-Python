N=1_125_001
def dels(n):
    s=set()
    for d in range(2,int(n**0.5)+1):
        if n%d==0 and d%10==7 and d!=7:
            s|={d}
        if n%(n//d)==0 and (n//d)%10==7 and (n//d)!=7:
            s |= {n//d}
    return sorted(s)

while True:
    if dels(N):
        print(N,dels(N)[0])
        # print(len(dels(N)))
    N+=1

# N=1_125_001
# def dels(n):
#     s=set()
#     for d in range(2,int(n**0.5)+21424):
#         if n%d==0:
#             s|={d,n//d}
#     return sorted(s)
#
#
# while True:
#     mas=dels(N)
#     t=[]
#     for el in mas:
#         if el%10==7 and el!=7:
#             t.append(el)
#     if len(t)>0:
#         print(N,min(t))
#
#     N+=21424