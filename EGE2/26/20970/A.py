f=open('26_20970.txt')
N,k=list(map(int,f.readline().split()))
mas=[]
for line in f:
    t0,dt,ms=map(int,line.split())
    mas.append([t0,dt,ms])
mas.sort()
zagr=[0]*k
deqs=[[] for i in range(k)]
util=0
for t0,dt,ms in mas:
    for j in range(k):
        while deqs[j]!=[] and deqs[j][0]<=t0:
            del deqs[j][0]

    if ms!=0:
        ind_mas=ms-1
    else:
        ind_mas=0
        min_len=10**9
        for i in range(k):
            if len(deqs[i])<min_len:
                min_len=len(deqs[i])
                ind_mas=i
    if deqs[ind_mas]==[]:
        deqs[ind_mas].append(t0+dt)
        zagr[ind_mas]+=1
    elif len(deqs[ind_mas])<5:
        deqs[ind_mas].append(deqs[ind_mas][-1]+dt)
        zagr[ind_mas] += 1
    else:
        util+=1
print(max(zagr),util)