from itertools import permutations

f=open('../../files/17_4417.txt')
mas=[int(i) for i in f]
par=permutations(mas,2)
k=0
mx=0
for x,y in par:
    if (x+y)%120==0:
        k+=1
        mx=max(mx,x+y)
print(k//2,mx)