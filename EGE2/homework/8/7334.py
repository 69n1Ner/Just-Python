from itertools import product, repeat
s=sorted('МЫСЛЬ')
k=0
for w in product(s,repeat=5):
    k+=1
    w=''.join(w)
    for i in range(1,len(w)):
        if w[:2]=='ЫЫ':
            print(w,k)
