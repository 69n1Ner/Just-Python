f=open('26_12495.txt')
data=[]
N,R,V=map(int,f.readline().split())
for l in f:
    data.append(int(l))
data.sort()
mas=[0]+data
mins=[10**7]*len(mas)
mins[0]=0
from collections import deque
deq=deque([0])
l=0
best_ref=10**9
last=-1
for i in range(1,len(mas)):
    while l<i and mas[l]<mas[i]-V:
        l+=1
    while deq and deq[0]<l:
        deq.popleft()
    if deq:
        mins[i]=mins[deq[0]]+1
    while deq and mins[i]<=mins[deq[-1]]:
        deq.pop()
    if mins[i]<=10**7:
        deq.append(i)
for i in range(1,len(mas)):
    if mas[i]+V>=R:
        if mins[i]<best_ref or (mins[i]==best_ref and mas[i]<last):
            best_ref=mins[i]
            last=mas[i]
print(best_ref,last)