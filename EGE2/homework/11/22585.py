from math import *
len=100
k=400_000
v1=30*1024*1024
v2=43*1024*1024
for i in range(2,100):
    v=ceil(i*len/8)*k
    if v1<=v<=v2:
        print(i)
k1=0
for i in range(65,256+1):
    k1+=1
print(k1)