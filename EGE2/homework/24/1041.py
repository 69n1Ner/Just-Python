f=open('../../files/24_1041.txt').readline()
from re import finditer
k=1
co=0
for i in range(0,len(f)):
    if f[i]=='f':
        co+=1
    if co==123:
        print(k)
        break
    k+=1
