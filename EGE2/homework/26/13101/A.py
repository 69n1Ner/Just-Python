f=open('26_13101.txt')
N=int(f.readline())
mas=[]
deq=[[],[]]
left=0
obs=0
for line in f:
    t0,dt,n=map(int,line.split())
    mas.append([t0,dt,n])
mas.sort()
for t0,dt,n in mas:
    deq[0]=[x for x in deq[0] if x > t0]
    deq[1] = [x for x in deq[1] if x > t0]
    if n==1 or (n==0 and len(deq[0])<=len(deq[1])):
        if len(deq[0])>=14:
            left += 1
            continue
        if len(deq[0])==0:
            deq[0].append(t0+dt)
        else:
            deq[0].append(max(deq[0])+dt)
    else:
        if len(deq[1]) >= 14:
            left+=1
            continue
        obs+=1
        if len(deq[1]) == 0:
            deq[1].append(t0 + dt)
        else:
            deq[1].append(max(deq[1]) + dt)
print(obs,left)

# print(max(mas,key=lambda x:x[2]))
