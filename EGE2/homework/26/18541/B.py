from collections import Counter

f = open('26_18541.txt')
N, M = map(int, f.readline().split())
dost = []
possible = []
t=[]

for _ in range(N):
    dost.append(int(f.readline()))
dost.sort()
for _ in range(M):
    mx = 0
    tmp=int(f.readline())
    if tmp in dost:
        t.append(tmp)
    else:
        for el in dost:
            if el >mx and el<=tmp:
                mx=el
            else:break
        t.append(mx)
sr = sum(t) / len(t)
tmp = Counter(t)
mx = 0
v = 0
for el in tmp.keys():
    if tmp[el] > mx:
        mx = tmp[el]
        v = el
print(int(sr), v)
