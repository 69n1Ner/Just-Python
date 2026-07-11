from collections import Counter

f=open('26_18541.txt')
N,M=map(int,f.readline().split())
dost=[]
possible=[]
for _ in range(N):
    dost.append(int(f.readline()))
for _ in range(M):

    possible.append(int(f.readline()))
dost.sort()
possible.sort()
t=[]
for el in possible:
    mx=-1
    for el2 in dost:
        if el2<=el:
            mx=max(mx,el2)
        else:break
    t.append(mx)
sr=sum(t)/len(t)
tmp=Counter(t)
mx=0
v=0
for el in tmp.keys():
    if tmp[el]>mx:
        mx=tmp[el]
        v=el
print(int(sr),v)