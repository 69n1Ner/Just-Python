from math import *
len=12
N=10+26+26
i=ceil(log2(N))
v=ceil(len*i/8)+28
k=20*1024/v
print(k)