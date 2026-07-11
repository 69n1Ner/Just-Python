f=open('26_18492.txt')
N=int(f.readline())
data=[list(map(int,l.split())) for l in f]
timeline=[0]*1441
for ida,st,en in data:
    for x in range(st,en):
        timeline[x]+=1
peak=max(timeline)
mas=[]
end=1
while end<1441:
    if timeline[end]==peak and timeline[end-1]<peak:
        start=end
        while timeline[end]==peak:
            end+=1
        mas.append((end-start,sum(n for n,st,en in data if start<=st<end or st<=start<en)))

    end+=1
print(len(mas),max(mas)[1])