f=open('../../files/24_17641.txt').readline()
from re import *
reg1=r'([1-9][0-9]*|0)'
reg2=fr'{reg1}([+*]{reg1})*'
s=[x.group() for x in finditer(reg2,f)]
s.sort(key=len)
mx=0
for el in s:
    # print(eval(el),el)
    if len(el)==142:
        print(eval(el),el)
    # if eval(el)==0:
    #     print()
    #     print(el)
    #     mx=max(mx,len(el))
