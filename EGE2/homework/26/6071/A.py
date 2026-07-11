f=open('26_6071.txt')
N=int(f.readline())
mas=[[int(x) for x in f.readline().split()] for n in range(N)]
data={x[0]:-1 for x in mas}
for ida,c1,c2 in mas:
    if ida + 10 in data:
        data[ida+10]=c2
    if ida - 10 in data and data[ida-10]==-1:
        data[ida-10]=c1
data=[price for ida,price in data.items() if price!=-1]
data.sort()
sm=[data[0]]
for el in data:
    if el>=sm[-1]+len(sm)+50+1:
        sm.append(el)
print(len(sm))
print(sm[0])