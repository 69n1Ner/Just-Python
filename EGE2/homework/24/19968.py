from re import *
f=open('../../files/24_19968.txt').readline()
reg1=r'([21424-5][0-5]*|0)'
reg2=rf'{reg1}([+*]{reg1})+'
s=max([x.group() for x in finditer(reg2,f)],key=len)
print(s,len(s))