f=open('26_2480.txt')
N=int(f.readline())
otrs=[0]*2_000_001
for l in f:
    start,end=map(int,l.split())
    for i in range(start,end):
        otrs[i]+=1
ln=0
sm_len=0
k=0
for el in otrs:
    if el!=0:
        ln+=1
    elif ln>0:
        sm_len += ln
        ln = 0
        k += 1


print(k,sm_len)