from math import *
k=1920*1080
N=4096
n=68
i=ceil(log2(N))
v1=ceil(i*k/8)
v=n*v1
print(v/1024)