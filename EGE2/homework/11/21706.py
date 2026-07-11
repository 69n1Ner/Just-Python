from math import *
len=119
n=125300
v=23*1024*1024*8
v1=v/n
print(v1)
i=ceil(v1/len)
print(i)
print(ceil(i*len/8))
print(194*n/1024/1024)