f=open('26_22577.txt')
N,M,K,V=map(int,f.readline().split())
data=[list(map(int,s.split())) for s in f]
mas=[[0]*(K+1) for m in range(M+1)]
for r,m in data:
    mas[r][m]=1
res=[[0]*(K+1) for m in range(M+1)]
for r in range(1,M+1):
    for m in range(1,K+1):
        res[r][m]=res[r-1][m]+mas[r][m]
        if m+2<=K and mas[r][m]==0 and mas[r][m+1]==0 and mas[r][m+2]==0:
            if res[r-1][m]>=V and res[r-1][m+1]>=V and res[r-1][m+2]>=V:
                print(r,m*3+3)
