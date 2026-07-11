from math import *
len1=2
len2=8
N1=18
N2=10
co=25
i1=ceil(log2(N1))
i2=ceil(log2(N2))

v1=i1*len1
v2=i2*len2
v3=ceil((v1+v2)/8)
v=co*v3
print(v)