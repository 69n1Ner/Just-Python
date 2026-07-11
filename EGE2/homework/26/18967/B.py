f=open('test.txt')
N,K=map(int,f.readline().split())
base=[]
for l in f:
    ida,time,co=map(int,l.split())
    base.append([ida,time,co])
base.sort(key=lambda x: (x[1],x[0]))
curr=N # текущее кол-во свободных мест в гардеробе
storage={}
last_op=0
left=0
occup=0
busy_t=0
busy_st=None
for el in base:
    ida,t,co=el[0],el[1],el[2]
    if ida not in storage:
        if occup+co<=N:
            storage[ida]=co
            occup+=co
            if occup==N:
                busy_st=t
        else:
            left+=co

    else:
        occup-=storage[ida]
        if busy_st is not None and occup<N:
            busy_t+=t-busy_st
            busy_st=None
print(left,busy_t)