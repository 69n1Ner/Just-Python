f=open('26_18967.txt')
N,K=map(int,f.readline().split())
base=[]
for l in f:
    ida,time,co=map(int,l.split())
    base.append([ida,time,co])
base.sort(key=lambda x: (x[1],x[0]))
left=0
curr=N # текущее кол-во свободных мест в гардеробе
blacklist=set()
passed=set()
last_op=0
k=0
for i in range(len(base)):
    # if base[i][0] in blacklist:
    #     continue
    if base[i][0] not in passed:
        if (curr-base[i][2])>=0:

            # if (curr-base[i][2])==0:
            #     last_op=base[i][1]
            # passed.add(base[i][0])
            curr-=base[i][2]

        else:
            blacklist.add(base[i][0])
            last_op+=base[i][2]

    else:
        if base[i][0] not in blacklist:
            curr+=base[i][2]
    passed.add(base[i][0])
    if curr==0:
        k+=base[i+1][1]-base[i][1]
print(last_op,k)

