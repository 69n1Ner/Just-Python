def del_sum_nech(n):
    s=[x for x in str(n) if x in '13579']
    if len(s)>0:
        return n%sum(map(int,s))==0
    else:return False
from re import *
reg=r'124[0-9]*5[0-9]*79'
for n in range(124579,130_000_00):
    if del_sum_nech(n) and fullmatch(reg,str(n))!=None:
        print(n,sum(map(int,str(n))))