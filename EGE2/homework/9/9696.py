from collections import *

f=open('../../files/9696.txt')
k=0
for l in f:
    fl=True
    line=l.split()
    co=0
    dic=Counter(line)
    if len(dic)==3:
        for e in line:
            mx1 = int(line.pop(line.index(max(line))))
            mx2 = int(line.pop(line.index(max(line))))
            mn1 = int(line.pop(line.index(min(line))))
            mn2 = int(line.pop(line.index(min(line))))
            if (mx2 + mx1) > 2 * (mn1 + mn2) and mx1 % mn1 != 0:
                k += 1
                break
print(k)

