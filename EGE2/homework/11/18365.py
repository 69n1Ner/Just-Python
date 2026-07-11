from math import *
len=28
N=505+7
i=ceil(log2(N))
vp=ceil(len*i/8)
vbg=117
vbm=35*6*1024
v=vp+vbg+vbm
v=v/1024/1024*10000
print(v)