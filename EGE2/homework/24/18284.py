from re import *
f1='REVVVLAAORRVEARRLBOLRVER'
f=open('../../files/24_18284.txt').readline()
reg=r'(?=([L][A-Z]*[O][A-Z]*[V][A-Z]*[E]))'
rg=compile(reg)
s=[x.group(1) for x in rg.finditer(f)]

print(s)
print(len(min(s,key=len)))