f=open('../../files/3362.txt')
k=0
for line in f:
    l=map(int,line.split())
    sm_c=0
    sm_n=0
    for el in l:
        if el%2==0:
            sm_c+=el
        else:
            sm_n+=el
    if sm_n>sm_c:
        k+=1
print(k)