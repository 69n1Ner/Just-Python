from collections import Counter
co=0
f=open('../../files/9539.txt')
for l in f:
    fl=True
    A=[]
    n=0
    line=l.split()
    k=Counter(line)
    if len(k)==3 :
        for key in k:
            if k[key]==1:
                n=int(key)
            else: A.append(int(key))
            if k[key]==3:
                fl=False
                break


        if fl:
            mn=min(A)
            mx=max(A)
            if mn<n<mx:
                co+=1
print(co)