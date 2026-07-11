from math import ceil

l_id=10
l_p=25
vd=48
k=1536
V=120*1024
v1=V/k
print(v1)
# v1=l_id*il_p*i ++
i=((v1-vd)*8)/(l_id+l_p)
print(i)
print(2**int(i))