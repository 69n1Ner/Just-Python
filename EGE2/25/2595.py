def f(x):
    s=set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            s|={i,x//i}
    return sorted(s)

N=400_000_001
while True:
    s=f(N)
    if len(s)>=5:
        pr=s[0]*s[1]*s[2]*s[3]*s[4]
        if pr%100==17 and pr <=N:
            print(pr,s[4])
    N+=1